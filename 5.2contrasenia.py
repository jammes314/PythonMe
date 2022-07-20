print('Inserta tu contrasenia, esta debe tener 8 caracteres, sin espacios.')
contrasennnia = input('Inserta tu contrasenia: ')
def contrasenia(contra):
    contador = 0
    for i in range(len(contra)):
        if contra[i] == " ":
            contador += 1
    
    if len(contra) < 8 or contador > 0:
        print('Contrasenia erronea')
    else:
        print('Contrasenia correcta')

contrasenia(contrasennnia)
             