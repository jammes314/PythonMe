# va generando objeto por objeto
# la instruccion yield construye un objeto iterable.
# es mas eficiente, busca un valor en especifico.
# utiles con listas de valores infinitos
# ////Sintaxis///////////////////

def generaNumerf(limite):
    num = 1 
    miLista = []
    while num < limite:
        miLista.append(num* 2)
        num += 1

    return miLista

print(generaNumerf(10))

def generaNumerg(limite):
    num = 1
    while num < limite:
        yield num*2

        num += 1
    
devuelvepares = generaNumerg(10)
print(next(devuelvepares))

print(next(devuelvepares))