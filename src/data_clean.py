import pandas as pd
import locale

class Data:
    """
    Base class for data operations.
    Manages the DataFrame and provides basic utilities.
    """
    def __init__(self, df_input: pd.DataFrame):
        self.df = df_input
    
    def get_data_types(self):
        """
        Returns a summary of DataFrame columns and their data types.
        """
        return self.df.info()
    
    def get_summary_stats(self):
        """
        Returns a descriptive statistical summary of the DataFrame.
        """
        return self.df.describe()
    
class DataCleaning(Data):
    """
    Performs all necessary data cleaning tasks.
    """
    def clean_data(self):
        """
        Executes the full data cleaning pipeline.
        
        Returns:
            pd.DataFrame: A cleaned DataFrame or None if an error occurs.
        """
        # Change column names to uppercase and strip whitespace
        self.df.columns = [col.upper().strip() for col in self.df.columns]

        # Convert the 'DATE' column to datetime objects
        try:
            # Set locale for month name parsing
            try:
                locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
            except locale.Error:
                locale.setlocale(locale.LC_TIME, 'C') # Fallback to a universal locale
            
            # Add a year to the date string for proper parsing
            self.df['DATE'] = self.df['DATE'].astype(str) + ' 2025'
            # Use mixed format for flexibility
            self.df['DATE'] = pd.to_datetime(self.df['DATE'], dayfirst=True, format='mixed')
            self.df['MONTH'] = self.df['DATE'].dt.month
        except Exception as e:
            print(f"Error: Could not format 'DATE' column. Details: {e}")
            return None 

        # Fill missing values
        if self.df.isnull().any().any():
            self.df = self.df.fillna(-1)
            print("Missing values have been filled with -1.")

        # Drop duplicate data
        if self.df.duplicated().any():
            self.df = self.df.drop_duplicates().reset_index(drop=True)
            print("Duplicate rows have been dropped.")
        
        # Identify and remove outliers based on IQR
        numeric_cols = self.df.select_dtypes(include=['number']).columns
        Q1 = self.df[numeric_cols].quantile(0.25)
        Q3 = self.df[numeric_cols].quantile(0.75)
        IQR = Q3 - Q1
        
        # Create a boolean mask to filter out outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Get the indices of rows containing outliers
        outlier_mask = (self.df[numeric_cols] < lower_bound) | (self.df[numeric_cols] > upper_bound)
        
        # Get the indices of rows containing outliers
        outliers_index = self.df[outlier_mask.any(axis=1)].index
        
        # Remove the identified outlier rows
        self.df = self.df.drop(outliers_index)
        print(f"{len(outliers_index)} outliers were removed from the dataset.")

        return self.df