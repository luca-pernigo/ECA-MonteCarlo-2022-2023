from logging import log
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from scipy.stats import expon

u=np.random.uniform(0,1,1000)
inv=-np.log(1-u)


# matplotlib histogram
plt.hist(inv,  color = 'green', edgecolor = 'black', density=True, bins = int(180/5))
u=np.linspace(0, 6.0, num=500)
finv=np.exp(-u)
plt.plot(u,finv, color="red")

# Add labels
plt.title('Exponential inverse method')
plt.xlabel('f(y)')
plt.ylabel('y')


