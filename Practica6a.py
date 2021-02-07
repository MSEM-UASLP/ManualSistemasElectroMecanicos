#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

import sympy as sym
from sympy.abc import s,t,x,y,z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform

# Transformada de Laplace (t->s)
U = laplace_transform(5*t, t, s)
print('U')
print(U[0])
# Resultado: 5/s**2

# Transformada inversa de Laplace (s->t)
X = inverse_laplace_transform(U[0],s,t)
print('X')
print(X)
# Resultado: 5*t*Heaviside(t)

# Función
F = 5*(s+1)/(s+3)**2
print('F')
print(F)
# Resultado: (5*s + 5)/(s + 3)**2

# Descomposición en fracciones parciales
G = sym.apart(F)
print('G')
print(G)
# Resultado: 5/(s + 3) - 10/(s + 3)**2

# Denominador de una función de transferencia
d1 = (s+1)*(s+3)*(s**2+3*s+1)

# Expandir polinomio
d2 = sym.expand(d1)
print('d2')
print(d2)
# Resultado: s**4 + 7*s**3 + 16*s**2 + 13*s + 3

# Encontrar raíces de un polinomio
print(sym.roots(d2))
# Resultado: {-1: 1, -3: 1, -3/2 - sqrt(5)/2: 1, -3/2 + sqrt(5)/2: 1}
