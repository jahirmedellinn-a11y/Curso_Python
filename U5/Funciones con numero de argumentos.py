#Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro.

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

#Las funciones son una herramienta fundamental en la programación y nos permiten estructurar y modularizar nuestro código. Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas en diferentes partes de nuestro programa.

#Además de las funciones definidas por el usuario, Python también proporciona una amplia gama de funciones incorporadas que podemos utilizar directamente, como print(), len(), range(), entre otras.