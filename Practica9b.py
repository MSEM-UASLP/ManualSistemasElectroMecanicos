#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.
#Código simulación sistema de dos partículas

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

k=0.2
m1=1
m2=1
b1=0.5
b2=0.9
t_stop = 30  # tiempo de simulación


#Modelo dinámico
def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    dydx[1] = -(b1*state[1]+b2*(state[1]-state[3])+k*(state[0]-state[2]))/m1
    dydx[2] = state[3]
    dydx[3] = -(b2*(state[3]-state[1])+k*(state[2]-state[1]))/m2
    return dydx

# tiempo
dt = 0.05
t = np.arange(0, t_stop, dt)

#condiciones iniciales
x10 = 2
x20 = 0
x30 = 3
x40 = 0

# estado inicial
state = [x10, x20,x30,x40]

# solución numérica
y = integrate.odeint(derivs, state, t)

x1 = y[:, 0]
x2 = y[:, 2]

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-6, 6), ylim=(-1, 1))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'tiempo = %.1fs'
time_text = ax.text(0.05, 0.5, '', transform=ax.transAxes)


def animate(i):
    li=1
    thisx = [x1[i],x2[i]+li]
    line.set_data(thisx,0)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
