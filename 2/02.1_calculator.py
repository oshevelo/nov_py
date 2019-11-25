def calculator():
    '''
    HW_2.1 simple calculator
    '''
    print('\nits very simple calculator')
    print('supported operators: +, -, *, /, **')
    print('PS enter 0 as operator to exit')

    while True:  # TODO get rid of 'while'?
        try:
            a = float(input('\ninput a: '))
            b = float(input('input b: '))
        except ValueError:
            print('a&b must be numbers')
        else:
            operator = input('operator: ')

            if operator == '+':
                print('result =', a+b)
            elif operator == '-':
                print('result =', a-b)
            elif operator == '*':
                print('result =', a*b)
            elif operator == '/':
                print('result =', a/b) if b else print('Error: zerro division')
            elif operator == '**':
                print('result =', pow(a, b))
            elif operator == '0':
                print('thanks for using the calculator')
                break
            else:
                print('operator is not supported')


if __name__ == '__main__':
    calculator()

# TODO test cases need
