#La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. Algunos ejemplos comunes incluyen:

#Math
#Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.

#Random
#Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.

#Datetime
#Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual