# Target Guided Ordinal Encoding 
import pandas as pd 

df = pd.DataFrame({
    'city' :  ['Chicago', 'Los Angeles', 'Chicago', 'Houston', 'Seattle'],
    'price' :[200,50,150,170,600]

})

#  calcyulate mean price of city 
mean =  df.groupby('city')['price'].mean().to_dict()
# print(mean)
#  replace ech city with its mean price
df['city_encoded'] = df['city'].map(mean)
print(df)

