# print('Programa de evaluacion de alumnos')
# notaAlumno = int(input())
# def evaluate(nota):
#     valoration = 'aprobada'
#     if nota < 5:
#         valoration = 'suspenso'
#     return valoration

# print(evaluate(notaAlumno))
# /////////////////////////////////////////
# from tkinter import E


# print('Verificacion de edad')
# edad = int(input('Itroduce tu edad porfa: '))
# if edad < 18:
#     print('No puedes pasar')
# elif edad > 100:
#     print('edad incorrecta, vuelvela a ingresar')
# else:
#     print('puedes pasar')

# # practica beca##########################
# print('Programa becas')
# distance = int(input('What is the distance from your home to the school'))
# print(distance)
# numofBrothers = int(input('Number of brother'))
# print(numofBrothers)
# salarioFam = int(input('FAmily salary'))

# def becasOnoBecas(cond1, cond2, cond3):
#     if distance > 40 and numofBrothers > 3 or salarioFam <= 20000:
#         print('Beca concedida')
#     else:
#         print('beca no concedida')

# becasOnoBecas(distance, numofBrothers, salarioFam)

# practica condicilnal 2 #################################
print('Asignaturas optativas')
print('Asignaturas optativas: tema1, tema2, tema3, tema4')
opcion = input( 'Escriba la asignatura elegida')
asignatura = opcion.lower()
if asignatura in ('tema1', 'tema2', 'tema3', 'tema4'):
    print('Asignatura escogida: '+ asignatura)
else:
    print('Asignatura no esta disponible')