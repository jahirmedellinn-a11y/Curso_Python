#La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.

contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break


