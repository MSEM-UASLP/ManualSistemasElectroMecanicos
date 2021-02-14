#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.
#Código doble péndulo

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G = 9.8  # aceleracion m/s^2
L1 = 1.0  # lngitud péndulo 1 en m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # masa de péndulo 1 en kg
M2 = 1.0  # masa de péndulo 2 en kg
t_stop = 5  # tiempo de simulación


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

# tiempo
dt = 0.05
t = np.arange(0, t_stop, dt)

# th1 y th2 son los ángulos iniciales en grados 
# w10 y w20 son las velocidades angulares en grados por segundo
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# estado inicial
state = np.radians([th1, w1, th2, w2])

# solución del modelo
y = integrate.odeint(derivs, state, t)

#posición de los eslabones
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'tiempo = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
