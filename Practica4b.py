#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
#multiplicacion de señales
baseline = plt.stem(x, np.cos(x), '-.')
plt.setp(baseline, 'color', 'k', 'linewidth', 2)
plt.title("Average=")
plt.ylabel("Sin[kT]")
plt.xlabel("kT")
plt.show()
#RMS de la señal graficada
print(np.sqrt(np.mean(np.cos(x))))
