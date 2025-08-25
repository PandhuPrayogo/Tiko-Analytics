import pandas as pd
import numpy as np
import seaborn as sbn

# File path
file_path = 'Files/Overview.xlsx'
print("==== Welcome to Tiko Analytics ====")
print("-----------------------------------")
# Checking File
try:
  df = pd.read_excel(file_path)
  print(f"File: '{file_path}' load succesfully")
  print("-----------------------------------")
  print(df.head(5))
  print(df.tail(5))
except FileNotFoundError:
  print(f"File: '{file_path}' is not found.")
except Exception as e:
  print(f"File: '{file_path}' is not succesfully load.")

