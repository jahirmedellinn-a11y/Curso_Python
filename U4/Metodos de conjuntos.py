#Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#add(elemento): agrega un elemento al conjunto.
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.

frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()