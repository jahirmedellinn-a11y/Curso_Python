#A medida que nuestros programas crecen en tamaño y complejidad, es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.

#Por ejemplo, podemos tener un módulo operaciones.py que contenga funciones relacionadas con operaciones matemáticas, y otro módulo utilidades.py que contenga funciones de uso general.

# operaciones.py
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)


def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")

#Luego, podemos importar y utilizar estas funciones en nuestro programa principal.

import operaciones
import utilidades


resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

