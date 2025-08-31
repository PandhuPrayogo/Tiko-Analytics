import locale
import pandas as pd

def clean_data(df):
  # Change name columns to uppercase
  old_columns = df.columns
  new_columns = []

  for i in old_columns:
    new_columns.append(i.upper())

  df.columns = new_columns
  # Formatting time and date
  try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
  except locale.Error:
    locale.setlocale(locale.LC_TIME, 'indonesian')
  
  df['DATE'] = df['DATE'] + ' 2025'
  
  df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True, format='%d %B %Y')

  # Check missing values
  check_null = df.isnull().sum().sum()
  if check_null == 0:
    pass
  else:
    df.fillna(-1)

  # Check duplicated data
  check_duplicate = df.duplicated().sum()
  if check_duplicate == 0:
    pass
  else:
    df.drop_duplicates()

  # Check outlier data
  Q1 = df['VIDEO VIEWS'].quantile(0.25)
  Q3 = df['VIDEO VIEWS'].quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  outliers = df[(df['VIDEO VIEWS'] < lower_bound) | (df['VIDEO VIEWS'] > upper_bound)]


  # Remove Outliers
  df_asli = df
  outliers_index = outliers.index
  df_asli.drop(outliers_index, inplace=True)
  
  return df
