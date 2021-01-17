# ----- CONDITIONALES -----
# Operadores de comparación : < > <= >= == !=
 
# if, else & elif ejecutan un código diferente dependiendo de las condiciones

age = 30
if age > 21:
    # Python utiliza identación para definir todo el código que se ejecuta dentro de el if
    print("You can drive a tractor trailer")
elif age >= 16:
    print("You can drive a car")
else:
    print("You can't drive")
 
# Condiciones con opearciones lógicas: and or not
if age < 5:
    print("Stay Home")
elif (age >= 5) and (age <= 6):
    print("Kindergarten")
elif (age > 6) and (age <= 17):
    print("Grade %d", (age - 5))
else:
    print("College")
 
# ----- STRINGS -----
 
# Combina cadenas con +
print("Hello " + "You")
 
# Obten la longitud de cadenas
str3 = "Hello You"
print("Length ", len(str3))
 
# obten el caracter en cierta posición
print("1st ", str3[0])
 
# último caracter
print("Last ", str3[-1])
 
# primeros tres caracteres
print("1st 3 ", str3[0:3]) 
 
# No puedes cambiar los valores de una cadena de esta manera
# str3[0] = "a" porque las cadenas son inmutables
# Pero si deseas modificar algo en una cadena puedes hacer lo siguiente
str3 = str3.replace("Hello", "Goodbye")
print(str3)
 
# verifica si cierta frase se encuentra en la cadena
print("you" in str3)
 
# Verifica si no se encuentra en la cadena
print("you" not in str3)
 
# Convierte una lista en una cadena y separa con espacios
print(" ".join(["Some", "Words"]))
 
# Convierte una cadena en una lista con un separador definido
print("A, string".split(", "))
 
# ----- LISTS -----
# Listas son un tipo de estructura que puede tener distintos tipos de datos o funciones
l1 = [1, 3.14, "Derek", True]
 
# Obtener longitud de la lista
print("Length ", len(l1))
 
# Otener el valor en un indíce
print("1st", l1[0])
print("Last", l1[-1])
 
# Cambiar el valor
l1[0] = 2
 
# Cambiar múltiples valores
l1[2:4] = ["Bob", False]
 
# Inserta un índice sin eliminar
# también puede ser l1.insert(2, "Paul")
l1[2:2] = ["Paul", 9]
 
# Agrega al final de la lista (También l1.extend([5, 6]))
l2 = l1 + ["Egg", 4]
 
# Remover un valor
l2.remove("Paul")
 
# Remover un índice
l2.pop(0)
print("l2", l2)
 
# Agrega al inicio (Puede ser también l1.append([5, 6]))
l2 = ["Egg", 4] + l1
 
# Lista de múltiples dimensiones
l3 = [[1, 2], [3, 4]]
print("[1, 1]", l3[1][1])
 
# Checar si cierto valor existe en la lista
print("1 Exists", (1 in l1))
 
# Encontrar el máximo o mínimo
print("Min ", min([1, 2, 3]))
print("Max ", max([1, 2, 3]))
