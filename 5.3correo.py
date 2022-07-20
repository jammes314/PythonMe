

correo = input('Insert your mail address')

def mailverifier(mail):
    arrobacounters = 0
    dotCounter = 0
    for i in range(len(mail)):
        if mail[i] == '@':
            arrobacounters += 1
        if mail[i] == '.':
            dotCounter += 1
    if arrobacounters > 1 and dotCounter != 1:
        print('Wrong mail')
    else:
        print('Correct mail')

mailverifier(correo)