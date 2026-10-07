#Para crear un conjunto, utiliza llaves o la función set():


frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
#Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}