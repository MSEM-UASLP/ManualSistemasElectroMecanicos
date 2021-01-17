#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

# ----- LOOPS -----
# While : Estos se ejecutan mientras la condición sea verdadera
w1 = 1
while w1 < 5:
    print(w1)
    w1 += 1
 
w2 = 0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        # Fuerza al loop a finalizar por completo
        break
    else:
        # forma reducida de escrbir i = i + 1
        w2 += 1
        # evita la siguiente iteración del loop (ciclo)
        continue
    w2 += 1
 
# Ciclo sobre una lista
l4 = [1, 3.14, "Derek", True]
while len(l4):
    print(l4.pop(0))
 
# For Loop
# Te permite desarrollar una accion un número de veces definido
# Range hace la acción 10 veces de 0 - 9
# end="" elimina el salto de línea
for x in range(0, 10):
    print(x, ' ', end="")
print('\n')
 
# Otra forma de hacer un ciclo a tráves de una lista imprimiendo directamente sus valores
l4 = [1, 3.14, "Derek", True]
for x in l4:
    print(x)
 
# Ciclo en una lista de números
for x in [2, 4, 6]:
    print(x)
 
# Para imprimr una lista bidimensional utilizamos dos loops
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
 
# ----- ITERATORS -----
# Puedes pasar un objeto a un "iterador" iter() el cual regresa un iterador que te permite ciclar 
l5 = [6, 9, 12]
itr = iter(l5)
print(next(itr)) #toma el siguiente valor
 
# ----- RANGES -----
# La función rango crea iteradores enteros
print(list(range(0, 5)))
 
# Puedes definir el paso de separación entre valores del rango
print(list(range(0, 10, 2)))
 
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
