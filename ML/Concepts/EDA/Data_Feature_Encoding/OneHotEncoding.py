
#one hot encoding 

from sklearn.preprocessing import OneHotEncoder
import pandas as pd 
df = pd.DataFrame({
    'color':  ['red', 'green', 'blue', 'red', 'green', 'blue'],
})
# print(df)
# create an instnce of encoder 
encoder =  OneHotEncoder()
# fit and transform the data
encoded_data = encoder.fit_transform(df[['color']]).toarray()
# print(encoded_data.toarray())
df2 = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out())
#print(df2)

# appending original with encoded data
a =  pd.concat([df, df2], axis=1)
print(a)
