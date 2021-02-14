
#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import numpy as np
import matplotlib.pyplot as plt

#multiplicacion de señales
x = np.linspace(0, 4*np.pi, 30)
baseline = plt.stem(x, np.sin(x)*np.exp(-x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Sinusoidal")
plt.ylabel("Sin[kT]")
plt.xlabel("kT")
plt.show()

#Suma de señales
x = np.linspace(0, 4*np.pi, 30)
baseline = plt.stem(x, np.sin(x)*np.exp(-x)+np.sin(50*x)*np.exp(-2*x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Sinusoidal")
plt.ylabel("Sin[kT]")
plt.xlabel("kT")
plt.show()
