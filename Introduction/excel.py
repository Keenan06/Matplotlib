import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('data.xlsx', sheetname='Sheet1')

x = list(df['X'])
y = list(df['Y'])