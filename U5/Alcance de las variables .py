#Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función. Por otro lado, las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa.

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.
