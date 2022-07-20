# # inmutables, no se pueden modificar despues
# # se pueden extraer porciones
# #se puede comprobar si un elemento esta en la tuple7
# # se pueden usar como claves en un diccionario
# # se escriben siempre entre parentesis

# from re import T


# Tuple1 = (1, 2, 3, 4, 5, 6, 7, 8,1)
# print(Tuple1)

# print(Tuple1[4])

# list = list(Tuple1)
# #de same way to turn a list into a tuple
# print(list)
# print(2 in Tuple1)
# print(Tuple1.count(1))
# print(Tuple1.index(1))

MyTupla = ('juan', 'maria', 'victoria')
#desempaquetado de tuplas
nombre1, nombre2, nombre3 = MyTupla
print(nombre1)
print(nombre2)
print(nombre3)