#Además de las excepciones incorporadas en Python, también puedes crear tus propias excepciones personalizadas. Esto es útil cuando deseas manejar situaciones específicas de tu programa.
#Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases.

def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")




