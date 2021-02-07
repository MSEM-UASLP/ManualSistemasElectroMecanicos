
#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t,C,R,u):
    dVodt = -u/(C*R)
    return dVodt
# initial condition
z0 = [0]

# number of time points
n = 1000

# time points
t = np.linspace(0,4*np.pi,n)

# input
u = np.sin(t)

# store solution
x = np.empty_like(t)
# record initial conditions
x[0] = z0[0]

L=0.01
R=0.5
C=0.1
# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = odeint(model,z0,tspan,args=(C,R,u[i]))
    # store solution for plotting
    x[i] = z[1]
    # next initial condition
    z0 = z[1]

# plot results
plt.plot(t,x,'b-',label=r'$\frac{dv_o}{dt}=-\frac{v_i}{RC}$')
plt.ylabel('$i_L(t)$')
plt.xlabel('t')
plt.legend(loc='best')
plt.show()
