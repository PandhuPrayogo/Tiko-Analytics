import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src import data_clean as dc
from src import desc_analyst as da

"""
Route to run this program: 
1. Data Cleaning:
  1.a Rename column to uppercase
  1.b Deleting redudant columns
  1.c Dropping Duplicates
  1.d Cleaning individual columns
  1.e Remove the NaN values from the dataset
  1.f Check for some more transformations
2. Fitur 1: Make a short information: Peak Video Views, Profile Views, Comments, Likes, Shares each month
3. Fitur 2: Check healty status based on the number 2
4. Fitur 3: Make a conclusion and suggestion based on number 3
"""

# File path
file_path = 'data/raw/Overview.xlsx'
print("==== Welcome to Tiko Analytics ====")
print("-----------------------------------")
# Checking File
try:
  df = pd.read_excel(file_path)
  print(f"File: '{file_path}' load succesfully")
  print("-----------------------------------")
  print(f"Old DataFrame: {df.head(5)}")
except FileNotFoundError:
  print(f"File: '{file_path}' is not found.")
except Exception as e:
  print(f"File: '{file_path}' is not succesfully load.")

# Data Cleaning
data_cleaning = dc.DataCleaning(df).clean_data()
print(data_cleaning)

print(da.DescriptiveAnalyst(data_cleaning).monthly_summary())

tedency_central = da.DescriptiveAnalyst(data_cleaning).central_tendency(df.columns)
print(da.DescriptiveAnalyst(df).print_formatted_stats(tedency_central))


# Fitur 2: Check healty status based on the Fitur 1:



