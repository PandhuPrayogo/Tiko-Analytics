import numpy as np
import pandas as pd
from src import data_clean as dc

class DescriptiveAnalyst:
  def __init__(self, df_input):
    self.df = df_input

  def monthly_summary(self):
        columns_to_analyze = ['VIDEO VIEWS', 'PROFILE VIEWS', 'LIKES', 'COMMENTS', 'SHARES']
        self.df['DATE'] = pd.to_datetime(self.df['DATE'])
        self.df['MONTH'] = self.df['DATE'].dt.month
      
        # Group by month and calculate descriptive statistics
        stats_monthly = self.df.groupby('MONTH')[columns_to_analyze].agg(
            ['sum', 'mean', 'median', 'std', 'max', 'min']
        ).astype(int)
        
        return stats_monthly
  
  def central_tendency(self, columns_name: list):
        """
        Calculates mean, median, and mode for specified columns.
        """
        stats = {}
        for col in columns_name:
            if col in self.df.columns:
                stats[col] = {
                    'mean': self.df[col].mean(),
                    'median': self.df[col].median(),
                    'mode': self.df[col].mode().iloc[0] if not self.df[col].mode().empty else 'N/A'
                }
        return stats
    
  def spread_tendency(self, columns_name: list):
        """
        Calculates variance, standard deviation, and IQR for specified columns.
        """
        stats = {}
        for col in columns_name:
            if col in self.df.columns:
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
        Prints the output dictionary in a clean, human-readable format.
        """
        for col, values in data.items():
            print(f"--- Kolom: {col} ---")
            for key, value in values.items():
                print(f"{key.replace('_', ' ').title():<20}: {value}")