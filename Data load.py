import pandas as pd
import numpy as np
# #load the data
bd = pd.read_csv('cars.csv', encoding= 'ISO-8859-1')
print(bd.head())
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
print(bd)