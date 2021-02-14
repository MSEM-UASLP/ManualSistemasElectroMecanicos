
#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

N=30 #Número de datos
x = np.linspace(0, 2*np.pi, N)
#multiplicacion de señales
baseline = plt.stem(x, np.cos(x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Average=")
plt.ylabel("Sin[kT]")
plt.xlabel("kT")
plt.show()
#Potencia de la señal discreta graficada
print(sp.sum(np.abs(np.cos(x))**2)/(2*N+1))
