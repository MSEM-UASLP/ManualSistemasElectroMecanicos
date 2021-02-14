#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import numpy as np
import matplotlib.pyplot as plt

#sinusoidal
x = np.linspace(0, 2*np.pi, 30)
baseline = plt.stem(x, np.sin(x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Sinusoidal")
plt.ylabel("Sin[kT]")
plt.xlabel("kT")
plt.show()

#exponencial
x = np.linspace(0, 10, 30)
baseline = plt.stem(x, np.exp(-x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Exponencial")
plt.ylabel("exp[-kT]")
plt.xlabel("kT")
plt.show()

#rampa
x = np.linspace(0, 10, 30)
baseline = plt.stem(x, x, '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Rampa")
plt.ylabel("kT")
plt.xlabel("kT")
plt.show()

#señal con valores aleatorios
x = np.linspace(1, 10,30)
def f(x):
    return np.sin(x) + np.random.normal(scale=0.1, size=len(x))

baseline = plt.stem(x, f(x),'-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Random")
plt.ylabel("y(kT)")
plt.xlabel("kT")
plt.show()

#señal impulso d(k-a)
def unit_impulse(a, n):
    delta = []
    for sample in n:
        if sample == a:
            delta.append(1)
        else:
            delta.append(0)

    return delta


a = 4  # retardo
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
d = unit_impulse(a, n)
plt.stem(n, d)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('d[n]')
plt.title('Impulso unitario d[4]')
plt.savefig("UnitImpulse.png") #guadra gráfico
plt.show()


# Escalón unitario u[n-a]
# LL y UL son los límites inferior y superior en el tiempo
def unit_step(a, n):
    unit = []
    for sample in n:
        if sample < a:
            unit.append(0)
        else:
            unit.append(1)
    return (unit)

a = 2  # retardo
UL = 10
LL = -10
n = np.arange(LL, UL, 1)
unit = unit_step(a, n)
plt.stem(n, unit)
plt.xlabel('n')
plt.xticks(np.arange(LL, UL, 1))
plt.yticks([0, 1])
plt.ylabel('u[n]')
plt.title('Escalón unitario u[n-a]')
plt.show()
