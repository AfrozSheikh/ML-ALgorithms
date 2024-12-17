# Normalizing the data 
#standardization 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
total_Bill = list(df["total_bill"])
mean = np.mean(total_Bill)
std = np.std(total_Bill)
# apply z-score formula for every data 
normalized_daata = [] 
for i in total_Bill:
    normalized_daata.append((i - mean) / std)

sns.histplot(normalized_daata)
plt.show()


# sam can be done by 
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scalar.fit(df[['total_bill']])
a = scalar.transform(df[['total_bill']])

