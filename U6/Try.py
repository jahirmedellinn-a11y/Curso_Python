#El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")