
from sklearn.preprocessing import MinMaxScaler
import numpy  as np
import seaborn as sns
df = sns.load_dataset('taxis')
min_max = MinMaxScaler()
a = min_max.fit(df[['distance' , 'fare']])
b=min_max.transform(df[['distance' , 'fare']])

# print(b)



