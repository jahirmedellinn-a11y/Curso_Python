#Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

#En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.
#También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.

from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0

