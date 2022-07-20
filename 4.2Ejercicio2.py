Nombre = input('Writte your name?')
Direccion = input('what is your Direccion')
Telephone = input('What is telephon?')

def DatosPersonales(nombre,direccion,telephone):
    listaDatosPersonales = []
    listaDatosPersonales.append(nombre)
    listaDatosPersonales.append(direccion)
    listaDatosPersonales.append(telephone)
    print(listaDatosPersonales)
print('Tus datos personales son:')
DatosPersonales(Nombre, Direccion, Telephone)