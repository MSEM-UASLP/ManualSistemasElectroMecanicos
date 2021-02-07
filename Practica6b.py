#Universidad Autónoma de San Luis Potosí Enero 2020

#----- INTRODUCCION -----
#Trata de ejecutar paso a paso cada una de las siguientes instrucciones y analizalas con ayuda de tu instructor de laboratorio.

# Transformada de Fourier utilizando numpy.fft method

import numpy as np
import matplotlib.pyplot as plotter

# Cuantos puntos son necesarios, Frecuencia de muestreo
samplingFrequency   = 100;

#A que intervalo de tiempo los puntos son muestreados
samplingInterval       = 1 / samplingFrequency;

#Tiempo de inicio de la señal
beginTime           = 0;

#Tiempo final de la señal
endTime             = 10; 

#Frecuencia de las señales
signal1Frequency     = 10;
signal2Frequency     = 20;

#Vector de tiempo
time        = np.arange(beginTime, endTime, samplingInterval);

#Crear dos señales sinusoidales
amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

#Generar subgráfico
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)

#Represeutación en el dominio del tiempo de la señal 1
axis[0].set_title('Señal con frecuencia 10Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Tiempo')
axis[0].set_ylabel('Amplitud')

# Time domain representation for sine wave 2
axis[1].set_title('Señal con frecuencia 20Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Tiempo')
axis[1].set_ylabel('Amplitud')

# Suma de señales
amplitude = amplitude1 + amplitude2

# Gráfico de la suma de las señales
axis[2].set_title('Señal con múltiples frecuencias')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Tiempo')
axis[2].set_ylabel('Amplitud')

# Representación en el dominio de la frecuencia
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalizamos la amplitud
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Excluimos el periódo de muestreo

tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Gráfico de la transformada de Fourier
axis[3].set_title('Transformada de Fourier mostrando los componentes de frecuencia')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frecuencia')
axis[3].set_ylabel('Amplitud')

plotter.show()
