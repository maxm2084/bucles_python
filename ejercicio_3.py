# CODE:22
# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con listas y bucles for

# Objetivo:
# Dado una lista de números, utilizar "for"
# para recorrer toda la lista y realizar 
# la sumatoria de todos los números

# Alumno:
# Usted ya cuenta con la lista numeros
# Crear una variable llamada suma_total
# inicializada en cero
# Realiza un bucle que recorra cada elemento
# En cada iteración incrementar el valor de suma_total
# (con el operador incremento) con cada número

# TIP
# Utilice el debugger para ver como avanza
# el programa paso a paso
numeros = [1, 5, -1, 6, 10, 2, -5]


# Imprimir en pantalla la variable suma_total
# El resultado final de la suma deberá ser 18
suma_total=0
for numero in numeros:
    suma_total += numero


print(suma_total)




