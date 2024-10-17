import numpy as np 
import matplotlib.pyplot as  plt
x = np.array([1,2,3,4,5])
from scipy.interpolate import interp1d


## interpolate  the data using linear interpolation 
# y = np.array([2,4,6,8,10])
# x_new = np.linspace(1,5,10)
# y_interp = np.interp(x_new , x,y)
# plt.scatter(x_new,y_interp)
# plt.show()


# cubic interpolation 
# y = np.array([1,8,27,64,125])
# f = interp1d(x,y , kind="cubic")
# x_new = np.linspace(1,5,45)
# y_interp = f(x_new) 
# plt.scatter(x_new,y_interp)
# plt.show()








