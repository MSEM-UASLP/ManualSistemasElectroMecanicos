#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

#Multiplicación de matrices
import numpy.matlib
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
np.dot(a,b)

#Determinante de una matriz
import numpy as np

b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print(b)
print(np.linalg.det(b))
print(6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2)) #Así harías el determinante a mano

#Solución de sistema de ecuaciones y cálculo de la inversa de una matriz
import numpy as np
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])

print('matriz a:')
print(a)
ainv = np.linalg.inv(a)

print('Inversa de a:')
print(ainv)

print('Matriz B:')
b = np.array([[6],[-4],[27]])
print(b)

print('Solucion:')
x = np.linalg.solve(a,b)
print(x)
# esta es la solució de la ecuacion
#Se puede encontrar la misma solución mediante
x = np.dot(ainv,b)
