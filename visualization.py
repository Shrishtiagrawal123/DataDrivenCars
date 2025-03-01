import pandas as pd
import numpy as np
# #load the data
bd = pd.read_csv('cars.csv', encoding= 'ISO-8859-1')
print(bd.head())
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
print(bd)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.pie(bd['cyl'].value_counts(), labels=bd['cyl'].value_counts().index, autopct='%1.1f%%')
plt.title('No. ofCylinders')
plt.show()

plt.figure(figsize=(10, 8))
plt.scatter(bd['disp'], bd['hp'])
plt.xlabel('Displacement')
plt.ylabel('Horspower')
plt.title('Displacement and Horspower')
plt.show()


plt.figure(figsize=(10, 8))
plt.boxplot(bd['mpg'])
plt.title('Mileage Distribution')
plt.show()

plt.figure(figsize=(10, 8))
plt.bar(bd['Model'].value_counts().index, bd['Model'].value_counts())
plt.xlabel('Model')
plt.ylabel('Number')
plt.title('No. of Model')
plt.show()

plt.figure(figsize=(10, 8))
plt.bar(bd['Model'].value_counts().index, bd['Model'].value_counts())
plt.xlabel('Model')
plt.ylabel('Number of Models')
plt.title('Model Distribution')
plt.xticks(rotation=90) 
plt.tight_layout()  
plt.show()
