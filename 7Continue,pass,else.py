# for letra in "Python":
#     if letra =="h":
#         continue
#     print("Vemos la letra: " + letra)


# nombre = "Pildoras Informaticas"
# contador = 0
# for i in nombre:
#     if i == " ":
#         continue
#     contador += 1
# print(contador)

email = input('introduce tu correo')
for i in email:
    
    if i == "@":
        arroba = True
        break
else:
    arroba = False
print(arroba)