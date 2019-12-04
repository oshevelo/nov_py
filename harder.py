def calc():
    def new():
        if d == '-':
            result = res - e
            print('We got: ' + str(result))
        elif d == '+':
            result = res + e
            print('We got: ' + str(result))
        elif d == '*':
            result = res * e
            print('We got: ' + str(result))
        elif d == '/':
            result = res / e
            print('We got: ' + str(result))
        else:
            print('Something went wrong')

    try:

        a = float(input('Enter first number: '))
        b = input('Available actions(+, -, *, /)\nEnter action: ')
        c = float(input('Enter second number: '))
        d = input('Available actions(+, -, *, /)\nEnter action: ')
        e = float(input('Enter third number: '))

        if b == '+':
            res = a + c
            new()

        elif b == '-':
            res = a - c
            new()

        elif b == '*':
            res = a * c
            new()

        elif b == '/':
            res = a / c
            new()

        else:
            print('Something went wrong')

    except ValueError or ZeroDivisionError:
        print('No way this will work')