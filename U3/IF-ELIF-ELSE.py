#La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones
#----------------------------------

calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")