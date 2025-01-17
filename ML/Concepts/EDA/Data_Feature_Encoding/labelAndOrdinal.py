# LabelEncoding 

from sklearn.preprocessing import LabelEncoder
import pandas as pd 

df = pd.DataFrame({
    'color':  ['red', 'green', 'blue', 'red', 'green', 'blue'],
})

#  create and instance of label encoder 
encoder =  LabelEncoder()

# encoding the categorical variable
label = encoder.fit_transform(df[['color']])
# print(label)

# Ordinal Encoding 
from sklearn.preprocessing import OrdinalEncoder
encoding = OrdinalEncoder(categories=[['green','red','blue']])
data = encoding.fit_transform(df[['color']])
print(data)