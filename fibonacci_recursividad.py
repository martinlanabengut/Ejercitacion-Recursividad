"""
Ejercicio 1
Escriba una función recursiva que tenga un parámetro n de tipo entero y que devuelva el n-ésimo
número de Fibonacci. Los números de Fibonacci se definen de la siguiente manera:
F0 = 0
F1 = 1
Fi+2 = Fi + Fi+1
"""
# fibonacci = 0, 1, 1, 2, 3, 5, 8, ...

def fibonacciRecursivo(n):
  if (n < 2):
    return n
  else:
    return(fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2))
