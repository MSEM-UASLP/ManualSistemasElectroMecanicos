
#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

#Solución de la ecuación dy/dt=-ky con k=0.3 y condición inicial y0=5 

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# funcion que regresa dy/dt
def model(y,t):
    k = 0.3
    dydt = -k * y**2
    return dydt

# condición inicial
y0 = 5

# puntos en el tiempo
t = np.linspace(0,20)

# solución ODE
y = odeint(model,y0,t)

# graficación
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()

#Código para variar un parámetro en nuestra ODE

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# función que regresa dy/dt
def model(y,t,k):
    dydt = -k * y
    return dydt

# condición inicial
y0 = 5

# tiempo
t = np.linspace(0,20)

# solución de ODEs con distinto parámetro k
k = 0.1
y1 = odeint(model,y0,t,args=(k,))
k = 0.2
y2 = odeint(model,y0,t,args=(k,))
k = 0.5
y3 = odeint(model,y0,t,args=(k,))

# resultados
plt.plot(t,y1,'r-',linewidth=2,label='k=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='k=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
