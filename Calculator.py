a = float(input('Enter a number: '))
b = float(input('Enter another number: '))

menu = 0

while menu !=9:
    print('''
    [1] Plus
    [2] Minus
    [3] Divied
    [4] Times
    [5] Exponent
    [6] Rooting
    [7] Percent
    [8] Another operation
    [9] Exit''')
    menu = int(input('Enter here: '))
    if menu == 1:
        print('{} plus {} is {}'.format(a, b, a+b))
    elif menu == 2:
        print('{} minimus {} is {}'.format(a, b, a-b))
    elif menu == 3:
        print('{} divied {} is {}'.format(a, b, a/b))
    elif menu == 4:
        print('{} times {} is {}'.format(a, b, a*b))
    elif menu == 5:
        print('{} to the power of {} is {}'.format(a, b, a ** b))
    elif menu == 6:
        print('The rooting of {} is and {} is {}'.format(a, a**0.5, b, b**0.5))
    elif menu == 7:
        print('{} percent of {} is {}'.format(a, b, (a *b /100))
    #elif menu == 8:
        a = float(input('Enter a number: '))
        b = float(input('Enter another number: '))
    #elif menu == 9:
        print('Exit')
    else:
        print('Error')