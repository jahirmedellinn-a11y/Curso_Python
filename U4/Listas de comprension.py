#Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

nueva_lista = [expresion for elemento in secuencia if condicion]


numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]