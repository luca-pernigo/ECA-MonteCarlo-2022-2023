

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import expon


n=10000
x=np.zeros(n)
x[0]=1


def gamma(x):
  return x**3*math.exp(-4*x)*4**4/math.gamma(4)

def exp(data, par):
  return (1/par)* math.exp(-(1/par)*data)

for i in range(n-1):
  u=np.random.uniform()
  x_star=np.random.exponential(x[i])
  A=min(1, gamma(x_star)*exp(x[i], x_star)/(gamma(x[i])*exp(x_star, x[i])))

  if u<=A:
    x[i+1]=x_star
  else:
    x[i+1]=x[i]

plt.xlim([0, 5])
plt.hist(x,  color = 'green', edgecolor = 'black', density=True, bins = int(50))

u=np.linspace(0, 6.0, num=500)
gammav=np.vectorize(gamma)
gammav(u)
plt.plot(u,gammav(u), color="red")

def normal(x):
  return 1/(math.sqrt(2*math.pi))*math.exp(-1/2*x**2)

for i in range(n-1):
  u=np.random.uniform()
  x_star=np.random.exponential(x[i])
  A=min(1, normal(x_star)*exp(x[i], x_star)/(normal(x[i])*exp(x_star, x[i])))

  if u<=A:
    x[i+1]=x_star
  else:
    x[i+1]=x[i]

plt.xlim([-3, 3])
plt.hist(x,  color = 'green', edgecolor = 'black', density=True, bins = int(50))


u=np.linspace(-3, 3.0, num=500)
normalv=np.vectorize(normal)
normalv(u)
plt.plot(u,normalv(u), color="red")

x[0:5001]=x[0:5001]*-1
x[4990:5009]

plt.xlim([-3, 3])
plt.hist(x,  color = 'green', edgecolor = 'black', density=True, bins = int(50))


u=np.linspace(-3, 3.0, num=500)
normalv=np.vectorize(normal)
normalv(u)
plt.plot(u,normalv(u), color="red")

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import expon


n=1000000
x=np.zeros(n)
x[0]=1


def p(x):
  return (0.5*math.exp(-0.2*x**2)+0.5*math.exp(-0.2*(x-10)**2))/math.sqrt(5*math.pi)
  #divide by sqrt 5 pi so that density integrates to one


def norm(x_star, x):
  return (1/math.sqrt(2*math.pi))* math.exp(-(1/2)*(x_star-x)**2)

for i in range(n-1):
  u=np.random.uniform()
  x_star=np.random.normal(x[i], 1)
  A=min(1, p(x_star)*norm(x[i], x_star)/(p(x[i])*norm(x_star, x[i])))

  if u<=A:
    x[i+1]=x_star
  else:
    x[i+1]=x[i]

plt.xlim([-5, 15])
plt.hist(x,  color = 'green', edgecolor = 'black', density=True, bins = int(50))



u=np.linspace(-5, 15, num=100)
pv=np.vectorize(p)
pv(u)
plt.plot(u,pv(u), color="red")

