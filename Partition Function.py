import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypsecant


delta = 1
boltzmann = 1.38064852e-23
T = np.linspace(0.01, 5)

### Two Level System - Internal Energy U
U = -(1/2) * np.tanh(1 /(2 * T))   # compute energy at temperature t
plt.plot(T, U)
plt.xlabel('Temperature')
plt.ylabel('Internal Energy')
plt.title('Two Level System - Internal Energy')
plt.grid(True)
plt.show()

### Two Level System - Heat Capacity C
C = ((delta / (2 * T))**2) * (1 / np.cosh(1 / (2 * T)))**2
plt.plot(T, C)
plt.xlabel('Temperature')
plt.ylabel('Heat Capacity')
plt.title('Two Level System - Heat Capacity')
plt.grid(True)
plt.show()

### Two Level System - Helmholtz Function F (double check)
F = - (boltzmann * T) * np.log((2 * np.cosh(1/2 * T)))
plt.plot(T, F)
plt.xlabel('Temperature')
plt.ylabel('Helmholtz Function')
plt.title('Two Level System - Helmholtz Function')
plt.grid(True)
plt.show()

### Two Level System - Entropy S
S = - U + F
# S = (((delta/2 * T) * 1/np.cosh(1/2 * T)) + (boltzmann * np.log(2 * np.cosh(1/2 * T))))
plt.plot(T, S)
plt.xlabel('Temperature')
plt.ylabel('Entropy')
plt.title('Two Level System - Entropy')
plt.grid(True)
plt.show()



### Two Level System - Pressure P

### Two Level System - Enthalpy H

### Two Level System - Gibbs Function G


