#Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo. Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:

#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b

#Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.

import mi_modulo


mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

