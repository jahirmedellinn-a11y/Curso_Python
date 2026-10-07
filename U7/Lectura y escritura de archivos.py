#Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#En este ejemplo, se abre el archivo "datos.txt" en modo de lectura utilizando open(). Luego, se lee todo el contenido del archivo utilizando el método read() y se almacena en la variable contenido. Finalmente, se muestra el contenido en la pantalla y se cierra el archivo utilizando el método close().

