import locale
import pandas as pd

class Data:
  def __init__(self, df_input):
    self.df = df_input
  
  def data_type(self):
    return self.df.info()
  
  def summarize_stats(self):
    return self.df.describe()
  
class DataCleaning(Data):
  def clean_data(self):
    # Change name columns to uppercase
    old_columns = self.df.columns
    new_columns = [i.upper() for i in old_columns]

    self.df.columns = new_columns
    # Formatting time and date
    try:
      locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
    except locale.Error:
      locale.setlocale(locale.LC_TIME, 'indonesian')
  
    self.df['DATE'] = self.df['DATE'] + ' 2025'
  
    self.df['DATE'] = pd.to_datetime(self.df['DATE'], dayfirst=True, format='mixed')

    # Check missing values
    check_null = self.df.isnull().sum().sum()
    if check_null == 0:
      pass
    else:
      self.df = self.df.fillna(-1)

    # Check duplicated data
    check_duplicate = self.df.duplicated().sum()
    if check_duplicate == 0:
      pass
    else:
      self.df = self.df.drop_duplicates()

    # Check outlier data per columns
    ## Video Views
    Q1 = self.df[self.df.columns].quantile(0.25)
    Q3 = self.df[self.df.columns].quantile(0.75)
    IQR = Q3 - Q1
        
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
        
    # Mendapatkan DataFrame dengan outlier
    outlier_data = self.df[(self.df[new_columns] < lower_bound) | (self.df[new_columns] > upper_bound)]
    
    old_data = self.df[outlier_data.any(axis=1)].index
    self.df.drop(old_data, inplace=True)

    return self.df
