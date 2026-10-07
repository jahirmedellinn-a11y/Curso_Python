#Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

#En este ejemplo, se abre el archivo "datos.txt" en modo de escritura utilizando open(). Luego, se escribe la cadena "¡Hola, mundo!" en el archivo utilizando el método write(). Finalmente, se cierra el archivo utilizando el método close().

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

