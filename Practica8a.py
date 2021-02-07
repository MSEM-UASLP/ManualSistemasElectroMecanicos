import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(z,t,L,C,R,u):
    dIldt = -z[1]/L+u/L
    dVcdt = z[0]/C-z[1]/(C*R)
    dzdt = [dIldt,dVcdt]
    return dzdt

z0 = [0.1,0]

# number puntos en el vector de tiempo
n = 501

# tiempo
t = np.linspace(0,5,n)

# step
u = np.zeros(n)
# cambio a 1.0 en t = 1.0
u[101:] = 1.0

# para guardar la solucion
x = np.empty_like(t)
y = np.empty_like(t)
# condiciones iniciales
x[0] = z0[0]
y[0] = z0[1]

L=0.01
R=0.5
C=0.1
# ODE
for i in range(1,n):
    tspan = [t[i-1],t[i]]
    z = odeint(model,z0,tspan,args=(L,C,R,u[i]))
    x[i] = z[1][0]
    y[i] = z[1][1]
    z0 = z[1]

plt.subplot(2, 1, 1)
plt.plot(t,x,'b-',label=r'$\frac{di_L}{dt}=-\frac{v_C}{L}+\frac{v_1}{L}$')
plt.ylabel('$i_L(t)$')
plt.xlabel('t')
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.plot(t,y,'r--',label=r'$\frac{dv_C}{dt}=\frac{i_L}{C}-\frac{v_C}{RC}$')
plt.ylabel('$v_C(t)$')
plt.xlabel('t')
plt.legend(loc='best')
plt.show()
