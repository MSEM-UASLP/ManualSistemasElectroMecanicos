#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

# ----- FUNCTIONS -----
# El uso de funciones nos permite reutilizar y organizar mejor nuestros códigos.

def get_sum(num1: int = 1, num2: int = 1):
    return num1 + num2
print(get_sum(5, 4))
 
# Acepta múltiples valores de entrada
def get_sum2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(get_sum2(1, 2, 3, 4))
 
# Regresa múltiples valores
def next_2(num):
    return num + 1, num + 2
i1, i2 = next_2(5)
print(i1, i2)
 
#Una función que crea otra función que múltiplica un valor dado

def mult_by(num):
    # Puedes crear funciones llamadas lambda (Es momento de googlear)
    return lambda x: x * num
print("3 * 5 =", (mult_by(3)(5)))
 
#Pasa una función a otra función
def mult_list(list, func):
    for x in list:
        print(func(x))
mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)
 
# Crea una lista de funciones
power_list = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

#Utiliza la función 1 de la lista anterior y evalúala en x=3
print(power_list[0](3))
