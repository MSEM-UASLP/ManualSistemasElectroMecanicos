
#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

#Código de la solución del conjunto de ecuaciones x0 = 0 y0 = 0, dxdt = (-x + u)/2.0 y dydt = (-y + x)/5.0 con u igual a una entrada escalón unitario
# que comienza en el segundo 5 y es de tamaño 2 esto es 2u(t-5)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# función que regresa la solución
def model(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x + u)/2.0
    dydt = (-y + x)/5.0
    dzdt = [dxdt,dydt]
    return dzdt

# condición incial
z0 = [0,0]

# número de puntos en el tiempo
n = 401

# tiempo
t = np.linspace(0,40,n)

# entrada escalón
u = np.zeros(n)
# cambia a 2.0 en t = 5.0
u[51:] = 2.0

# guarda la solución
x = np.empty_like(t)
y = np.empty_like(t)
# condiciones iniciales
x[0] = z0[0]
y[0] = z0[1]

# resuelve la ecuación
for i in range(1,n):
    # espacio de tiempo para la siguiente integración
    tspan = [t[i-1],t[i]]
    # resuelve el siguiente instante
    z = odeint(model,z0,tspan,args=(u[i],))
    # guarda la solución para graficar
    x[i] = z[1][0]
    y[i] = z[1][1]
    # siguiente condición inicial
    z0 = z[1]

#resultados
plt.plot(t,u,'g:',label='u(t)')
plt.plot(t,x,'b-',label='x(t)')
plt.plot(t,y,'r--',label='y(t)')
plt.ylabel('values')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
