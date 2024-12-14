import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
marks = [1,2,3,4,]-699,5,6,7,55,8,9,10,11,89,100
# lower_fence ---> higher fence 
min , q1 , q2 ,q3,max = np.quantile(marks , [0,0.25,0.5,0.75,1.0])

Iqr = q3-q1 
lower_fence = q1-1.5*(Iqr)
upper_fence = q3+1.5*(Iqr)
a =1  
sns.boxplot(marks)
# print(lower_fence , upper_fence)
outliers =[]
for  i in marks:
    if i>=lower_fence and  i<=upper_fence:
        a = a+1
    else:
        outliers.append(i)

print(outliers)
plt.show()



