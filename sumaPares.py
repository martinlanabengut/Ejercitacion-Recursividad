"""
Ejercicio 3
Escribir un programa que encuentre la suma de los enteros positivos pares desde N hasta 2.
Chequear que si N es impar se imprima un mensaje de error.
"""
def sumaPares(numero):
  if(numero == 2):
    return 2
  else:
    return (numero + sumaPares(numero-2))  