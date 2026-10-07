#El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")