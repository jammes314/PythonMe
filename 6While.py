# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter a second number bigger than the last one '))

# def Bignummer(num1, num2):
#     while num2 > num1:
#         num1 = num2
#         num2 = int(input('Escribe un numero mayor al anterior: '))
    
#     print(num2, ' no es mayor que ', num1)

# Bignummer(num1, num2)
######################

# import math

# print('Programa calculo raiz cuadrada')
# numero = int(input('Enter the number that ypu want to know the root'))
# intentos = 0

# while numero < 0 : 
#     print('No se puede hallar la raiz de un num negativo')

#     if intentos == 2:
#         print('Muchos intentos, el programa finalizo')
#         break
#     numero = int(input('Enter the number that ypu want to know the root'))
#     if numero <0 :
#         intentos += 1
# if intentos < 2 :
#     solucion = math.sqrt(numero)
#     print('La raiz cuadrada de {} es : {}'.format(numero, solucion))
###############################################################################

numero = int(input('Enter any number'))


def sumPositiveNum(num):
    suma = 0
    while num > 0:
        suma += num
        num = int(input('Enter another number'))
    print('Suma: {}'.format(suma))

sumPositiveNum(numero) 