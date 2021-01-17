#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

#Graficación de una serie de datos
import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,11) #Se crea un vector de 1 al 11 con incrementos unitarios
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y) 
plt.show()

#Misma gráfica que el código anterior pero gráfica puntos
import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,"ob") 
plt.show() 

#Gráfica de una función sinusoidal
import numpy as np 
import matplotlib.pyplot as plt  

x = np.arange(0, 3 * np.pi, 0.1) #Vecotr de 0 a 3 veces pi con incrementos de 0.1
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y) 
plt.show() 

#Gráficas con subgráficos
import numpy as np 
import matplotlib.pyplot as plt  
   
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
   
plt.subplot(2, 1, 1)
   
plt.plot(x, y_sin) 
plt.title('Sine')  
   
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
plt.show()

#Gráfico de barras
from matplotlib import pyplot as plt 
x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()
