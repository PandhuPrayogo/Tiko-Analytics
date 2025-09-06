import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src import data_clean as dc
from src import desc_analyst as da

"""
Program Route: 
1. Data Loading & Cleaning
   - Renaming columns to uppercase.
   - Removing redundant data and duplicates.
   - Handling missing values (NaNs).
   - Checking for outliers.
2. Descriptive Analytics
   - Summarizing monthly key metrics (Views, Likes, Comments, Shares).
   - Calculating measures of central tendency (Mean, Median, Mode).
   - Calculating measures of spread (Variance, Std Dev, IQR).
3. Business Insights
   - Checking for account health status.
   - Drawing conclusions and providing suggestions.
"""

# File path
file_path = 'data/raw/Overview.xlsx'
print("==== Welcome to Tiko Analytics ====")
print("-----------------------------------")

df = None
try:
    df = pd.read_excel(file_path)
    print(f"File: '{file_path}' loaded successfully.")
    print("-----------------------------------")
    print("Original DataFrame:")
    print(df.head(5))
except FileNotFoundError:
    print(f"Error: File '{file_path}' is not found.")
except Exception as e:
    print(f"Error: File '{file_path}' failed to load.")
    print(f"Details: {e}")

# ---
## Data Cleaning

if df is not None:
    print("\n==== Starting Data Cleaning ====")
    # Instantiate DataCleaning class and run the cleaning process
    cleaned_df = dc.DataCleaning(df).clean_data()
    print("-----------------------------------")
    print("Cleaned DataFrame:")
    # Check if the cleaning process was successful before printing
    if cleaned_df is not None:
        print(cleaned_df.head(5))

        # Instantiate DescriptiveAnalyst with the cleaned data
        analyzer = da.DescriptiveAnalyst(cleaned_df)
        
        # ---
        ## Descriptive Analytics

        # Feature 1.0: Monthly Summary
        print("\n ==== Statistic Descriptive ====")
        print("\n==== Monthly Summary ====")
        monthly_summary_stats = analyzer.monthly_summary()
        if monthly_summary_stats is not None:
            print(monthly_summary_stats)
        
        # Define the columns for analysis
        columns_to_analyze = ['VIDEO VIEWS', 'PROFILE VIEWS', 'LIKES', 'COMMENTS', 'SHARES']
        
        # Feature 1.1: Central Tendency
        print("\n==== Central Tendency ====")
        central_stats = analyzer.central_tendency(columns_to_analyze)
        analyzer.print_formatted_stats(central_stats)

        # Feature 1.2: Spread Tendency
        print("\n==== Spread Tendency ====")
        spread_stats = analyzer.spread_tendency(columns_to_analyze)
        analyzer.print_formatted_stats(spread_stats)

    print("\n==== Data Analysis Completed ====")