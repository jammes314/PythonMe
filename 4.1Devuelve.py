num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

def DevuelveMax(n1, n2):
    if n1 < n2:
        print(n2)
    elif n1 > n2:
        print(n1)
    else:
        print('are the same numbers')
print('The highest number is:')

DevuelveMax(num1, num2)
