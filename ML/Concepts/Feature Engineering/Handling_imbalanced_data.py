
import numpy as np 
import pandas as pd 
from sklearn.utils import resample

# creating imbalanced dataset 
np.random.seed(123)
nsamples = 1000 
class0ratio = 0.9 
nclass0 = int(nsamples * class0ratio)
nclass1  = nsamples - nclass0

class0 = pd.DataFrame({
    'feature1' : np.random.normal(loc=0, scale=1 , size=nclass0),
    'feature2' : np.random.normal(loc=0, scale=1 , size=nclass0),
    'target':[0] *nclass0
})

class1 = pd.DataFrame({
    'feature1' : np.random.normal(loc=2, scale=1 , size=nclass1),
    'feature2' : np.random.normal(loc=2, scale=1 , size=nclass1),
    'target':[1] *nclass1
})

df = pd.concat([class0, class1]).reset_index(drop=True)
# print(df.head())


df_minority  = df[df['target'] == 1]
df_majority = df[df['target']== 0 ]

# print(df_minority.head())
# upsampling
df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority) , random_state=42)
# print(df_minority_upsampled['target'].value_counts())
df_upsampled = pd.concat([df_majority , df_minority_upsampled])
# print(df_upsampled['target'].value_counts())
# print(df_upsampled.shape)



# down sampling 
# maximum data ko kam karte he 
class2 = pd.DataFrame({
    'feature1' : np.random.normal(loc=0, scale=1 , size=nclass0),
    'feature2' : np.random.normal(loc=0, scale=1 , size=nclass0),
    'target':[0] *nclass0
})

class3 = pd.DataFrame({
    'feature1' : np.random.normal(loc=2, scale=1 , size=nclass1),
    'feature2' : np.random.normal(loc=2, scale=1 , size=nclass1),
    'target':[1] *nclass1
})

df = pd.concat([class2, class3]).reset_index(drop=False)
df_majority_downsampled = resample(df_majority, replace=True, n_samples=len(df_minority) , random_state=42)

df_downsampled = pd.concat([df_minority , df_majority_downsampled])
print(df_downsampled['target'].value_counts())