import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from src import data_clean as dc
from src import desc_analyst as da
from src import business as bs

"""
Program Flow: 
1. Data Loading & Cleaning
   - Rename columns to uppercase.
   - Remove redundant and duplicate data.
   - Handle missing values (NaNs).
   - Check for outliers.
2. Descriptive Analytics
   - Summarize monthly key metrics (Views, Likes, Comments, Shares).
   - Calculate measures of central tendency (Mean, Median, Mode).
   - Calculate measures of spread (Variance, Std Dev, IQR).
3. Business Insights
   - Check for account health status.
   - Draw conclusions and provide suggestions.
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
    exit()
except Exception as e:
    print(f"Error: File '{file_path}' failed to load.")
    print(f"Details: {e}")
    exit()

# Data Cleaning
if df is not None:
    print("\n==== Starting Data Cleaning ====")
    # Instantiate DataCleaning class and run the cleaning process
    cleaned_df = dc.DataCleaning(df).clean_data()
    if cleaned_df is None:
        print("Data cleaning failed. Exiting program.")
        exit()
        
    print("-----------------------------------")
    print("Cleaned DataFrame:")
    print(cleaned_df.head(5))

    # Instantiate DescriptiveAnalyst with the cleaned data
    analyzer = da.DescriptiveAnalyst(cleaned_df)
    
    # Descriptive Analytics
    # Feature 1.0: Monthly Summary
    print("\n==== Descriptive Statistics ====")
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

    # Business Insights
    print("\n==== Business Insights ====")
    engagement_columns = ['LIKES', 'COMMENTS', 'SHARES']
    business_insight = bs.Business(cleaned_df)
    
    # Calculate metrics
    total_engagement = business_insight.get_total_engagement(engagement_columns)
    total_video_views = cleaned_df['VIDEO VIEWS'].sum()
    total_profile_views = cleaned_df['PROFILE VIEWS'].sum()
    
    engagement_rate = business_insight.engagement_rate(total_engagement, total_video_views)
    conversion_rate = business_insight.conversion_rate(total_profile_views, total_video_views)

    # Status checking
    followers_total = 2180
    rate_data = bs.StatusRate(cleaned_df)
    account_status = rate_data.get_account_status(followers_total)

    # Print results
    print("\nAccount Status Summary:")
    for key, value in account_status['ACCOUNT STATUS SUMMARY'].items():
        print(f"{key}: {value}")
    
    print("\nBusiness Strategy:")
    for kpi in account_status['BUSINESS STRATEGY']['KEY PERFORMANCE INDICATORS (KPI)']:
        print(f"- {kpi}")
    
    print("\nKey Performance Indicators and Objectives and Key Results:")
    for okr in account_status['BUSINESS STRATEGY']['OBJECTIVES AND KEY RESULTS (OKR)']:
        print(f"Objective: {okr['Objective']}")
        for kr in okr['Key Results']:
            print(f"- {kr}")

print("\n==== Data Analysis Completed ====")
