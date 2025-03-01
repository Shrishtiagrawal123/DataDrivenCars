import pandas as pd
import numpy as np
#load the data
bd = pd.read_csv('cars.csv', encoding= 'ISO-8859-1')
print(bd.head())
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
print(bd)
 # Display the no.of row and column
print("Number of Rows:",bd.shape[0])
print("Number of columns:",bd.shape[1])
#interpretation in 25% and 75% 
bd= bd.dropna()
percentile_25 = np.percentile(bd['mpg'], 25)
percentile_75 = np.percentile(bd['mpg'], 75)
print('Interpretation in 25%', percentile_25)
print('Interpretation in 75%', percentile_75)
# # Analyze the data using statistics such as Mean ,Median,SD(standard Deviation)
# Calculate Mean
print("Mean:",bd['disp'].mean())
# Calculate Median
print("Median:",bd['disp'].median())
# Calculate standard Deviation
print("Standard Deviation:",bd['disp'].std())