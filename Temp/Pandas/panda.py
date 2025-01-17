

import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.head()) 
















# # import pandas as pd  
# import numpy as np 
# import matplotlib.pyplot as plt
# import seaborn as sns 
# ti  = sns.load_dataset("titanic")

# x = np.linspace(0,10,11) 
# y = np.sin(x) 
# z = plt.plot(x,y) 
# print(plt.show())
# x = [1,2,9,4]
# plt.xlabel("DDDDDDDDDdd")
# y= [5,15,3,4]
# z = plt.plot(x,y)
# plt.show()

# df = pd.read_csv("titanic.csv") 

# d = df[['Pclass' , 'Sex','Age']][0:3]
# e = df[['Pclass' , 'Sex','Age']][3:5]
# f = pd.concat([d,e])

# print(e)

# a =c[ c['Age']<18 ]
# d = df[(df['Age']<10) & (df["Sex"]=="female")]
# e =d[['Name']]
# print(e)

# a = pd.DataFrame({
#     'key1':[1,2,3,4] , 
#     'key2' : [5,6,7,8],
#     'key3' : [9,9,9,9]
# })
# b= pd.DataFrame({
#     'key1':[1,22,3,4] ,
#     'key5' : [15,16,17,18],
#     'key6' : [19,19,19,19]
# })
# c  = pd.merge(a,b)
# print(c)
# a = sns.heatmap(ti.isnull())
# plt.show()


