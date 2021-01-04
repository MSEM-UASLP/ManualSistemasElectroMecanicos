#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.
# Los archivos de python terminan con extensión .py

# Imprimir en consola
print("Hello World")
 
# Leer de consola, guardar en una variable y usarla
name = input("What is your name ")
print("Hi ", name)
 
# una oración en múltiples lineas
v1 = (
        1 + 2
        + 3
)
v1 = 1 + 2 \
     + 3
print(v1)
 
# Operaciones
v1 = 5;
v1 = v1 - 1
 
"""
Comentario de 
múltiples lineas
"""
 
# ----- VARIABLES -----
# Las variables son nombres asignados a valores
# El primer caracter del nombre de una variable debe ser un _ o una letra
v2 = 1
V2 = 2  # v1 es diferente de V2
 
# Se puede asignar a múltiples variables
v3 = v4 = 20
 
# ----- Tipos de datos -----
 
#Obtener el tipo
print(type(10))
 
# Tamaño máximo en una variable
print(sys.maxsize)
 
# Floats son valores con decimales
# El máximo flotante que se puede almacenar se obtiene de
print(sys.float_info.max)
 
 
# Números complejos z=a+jb
cn1 = 5 + 6j
 
# Booleanos
b1 = True
 
# Strings se dentifican con ' o "
str1 = "Escape Sequences \' \t \" \\ and \n"
 
str2 = '''Triple quoted strings can contain ' and "'''
 
# Cambiar tipo de variable
print("Cast ", type(int(5.4)))  # a int
print("Cast 2 ", type(str(5.4)))  # a string
print("Cast 3 ", type(chr(97)))  # a string
print("Cast 4 ", type(ord('a')))  # a int
 
# ----- OUTPUT -----
# Definir separador en print
print(12, 21, 1974, sep='/')
 
# Eliminar salto de línea
print("No Newline", end='')
 
# Formato de cadena
print("\n%04d %s %.2f %c" % (1, "Derek", 1.234, 'A'))
