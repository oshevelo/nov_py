def calculator():  # TODO ast!
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['+', '-', '*', '/']
    chars = ['.', 'p', 'i', 'e']
    parentheses = ['(', ')']

    allowed_characters = digits + operators + chars + parentheses

    raw_str = input('math ')
    for each in raw_str:
        if each not in allowed_characters:
            raise Exception

    result = 'Something wrong...'
    try:
        result = eval(raw_str, {'__builtins__': {}})
    except SyntaxError:
        print('SyntaxError in your expression. Try again')
    except ZeroDivisionError:
        print('ZeroDivisionError in your expression. Try again')
    finally:
        print(raw_str, '=', result)


if __name__ == '__main__':
    calculator()
