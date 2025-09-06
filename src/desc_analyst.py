import numpy as np
import pandas as pd

class DescriptiveAnalyst:
    """
    Performs descriptive analytics on a given DataFrame.
    """
    def __init__(self, df_input):
        self.df = df_input

    def monthly_summary(self):
        """
        Calculates a monthly summary for key performance metrics.
        
        Returns:
            pd.DataFrame: A DataFrame with aggregated monthly stats.
        """
        # Columns to analyze for monthly summary
        columns_to_analyze = ['VIDEO VIEWS', 'PROFILE VIEWS', 'LIKES', 'COMMENTS', 'SHARES']
        
        # Group by month and calculate descriptive statistics
        stats_monthly = self.df.groupby('MONTH')[columns_to_analyze].agg(
            ['sum', 'mean', 'median', 'std', 'max', 'min']
        ).astype(int)
        
        return stats_monthly
    
    def central_tendency(self, columns_name: list):
        """
        Calculates mean, median, and mode for specified columns.
        
        Args:
            columns_name (list): A list of column names to analyze.
        
        Returns:
            dict: A dictionary containing the central tendency stats for each column.
        """
        stats = {}
        for col in columns_name:
            if col in self.df.columns and pd.api.types.is_numeric_dtype(self.df[col]):
                stats[col] = {
                    'mean': self.df[col].mean(),
                    'median': self.df[col].median(),
                    'mode': self.df[col].mode().iloc[0] if not self.df[col].mode().empty else 'N/A'
                }
        return stats
    
    def spread_tendency(self, columns_name: list):
        """
        Calculates variance, standard deviation, and IQR for specified columns.
        
        Args:
            columns_name (list): A list of column names to analyze.
        
        Returns:
            dict: A dictionary containing the spread stats for each column.
        """
        stats = {}
        for col in columns_name:
            if col in self.df.columns and pd.api.types.is_numeric_dtype(self.df[col]):
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                stats[col] = {
                    'variance': self.df[col].var(),
                    'standard_deviation': self.df[col].std(),
                    'IQR': IQR
                }
        return stats
    
    def print_formatted_stats(self, data: dict):
        """
        Prints a dictionary of statistical results in a clean, human-readable format.
        """
        for col, values in data.items():
            print(f"--- Column: {col} ---")
            for key, value in values.items():
                print(f"{key.replace('_', ' ').title():<20}: {value}")
            print("\n")