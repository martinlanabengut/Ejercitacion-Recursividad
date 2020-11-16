"""
Ejercicio 2
Escribir una función recursiva que devuelva la suma de los primeros N enteros. Se debe pedir la carga
de N como un valor entero positivo.
"""

def sumaNenteros(n):
  if (n < 2):
    return 1
  else:
    return( n + sumaNenteros(n-1))
