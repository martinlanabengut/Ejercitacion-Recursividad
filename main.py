"""
Ejercicio 1
Escriba una función recursiva que tenga un parámetro n de tipo entero y que devuelva el n-ésimo
número de Fibonacci. Los números de Fibonacci se definen de la siguiente manera:
"""

from fibonacci_recursividad import fibonacciRecursivo
from sumaNenteros import sumaNenteros
from sumaPares import sumaPares

n = 3

print(fibonacciRecursivo(n))

"""
Ejercicio 2
Escribir una función recursiva que devuelva la suma de los primeros N enteros. Se debe pedir la carga
de N como un valor entero positivo.
"""
n = 5 

print(sumaNenteros(n))

"""
Ejercicio 3
Escribir un programa que encuentre la suma de los enteros positivos pares desde N hasta 2.
Chequear que si N es impar se imprima un mensaje de error.
"""
numero = 8

print(sumaPares(numero))
