#Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función input(). Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

#En este ejemplo, se solicita al usuario que ingrese su nombre y edad utilizando la función input(). Los valores ingresados se almacenan en las variables nombre y edad, respectivamente. Luego, se utilizan estas variables para mostrar un saludo personalizado en la pantalla.

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

