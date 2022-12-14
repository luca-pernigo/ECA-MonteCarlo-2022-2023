

import numpy as np

# Parameters

S0 = 102 #Stock price today
K = 100 #Strike
T = 1.0 #unit
r = 0.02 #risk free rate
sigma = 0.15 #volatility rate

#interval at which end there is the expiration of our european option
M = 30;
dt = T / M; 

# number of simulations
I = 10000
# Simulating I paths with M time steps

S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt+ sigma * math.sqrt(dt)* random.standard_normal((M + 1, I)), axis=0))
#calculate I simulations of S



# Calculating the Monte Carlo estimator
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I

#take average of returns and bring back to today with continous rate

# Results output

print('The European Option Value is: ', C0)  # The European Option Value is:  8.165807966259603

random.standard_normal((M + 1, I)).shape

import matplotlib.pyplot as plt
plt.plot(S[:, :1000])
plt.grid(True)
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
