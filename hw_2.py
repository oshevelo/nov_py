
# 1. input a input b input op -> result
i = 5
while i != 0:
    try:  # пытаемся привести введенные числа к занчению числа, если введено не число, говорим об ошибки и даем всего 5 попыток
        a = float(input('введите число'))
        b = float(input('введите второе число'))
    except ValueError:
        i -= 1
        print(f'это не число, введите, число. у вас осталось {i} попыток')
    else:
        oper = input('введите желаемую операцию - + / или *')  # проверяем что бы ввели мат.операцию, с кол-вом попыток продолжаем
        if oper not in ('+', '-', '/', '*'):
            i -= 1
            print(f'извините вы ввели не математическую операцию, начните заново у вас осталось {i} попыток')
        else:
            i = 0
            if oper == '/':
                if b == 0:
                    print('извините, деление на ноль не возможно')  # в случае деления, проверяем что бы делитель не был = 0
                else:
                    res = a / b
                    print(res)
            elif oper == '+':
                res = a + b
                print(res)
            elif oper == '-':
                res = a - b
                print(res)
            elif oper == '*':
                res = a * b
                print(res)


# 2. #1 +  скобки

i = 5
while i != 0:
    try:  # пытаемся привести введенные числа к занчению числа, если введено не число, говорим об ошибки и даем всего 5 попыток
        a = float(input('введите первое число выражения в скобках'))
        b = float(input('введите второе число выражения в скобках'))
    except ValueError:
        i -= 1
        print(f'это не число, введите, число. у вас осталось {i} попыток')
    else:
        oper = input('введите желаемую операцию - + / или * для выражения в скобках')
        if oper not in ('+', '-', '/', '*'):
            i -= 1
            print(f'извините вы ввели не математическую операцию, начните заново у вас осталось {i} попыток')  # проверяем что бы ввели мат.операцию, с кол-вом попыток продолжаем
        oper2 = input('введите желаемую операцию - + / или * которая полседует за скобками')  # тут так же проверяем что бы это была мат. операция
        if oper2 not in ('+', '-', '/', '*'):
            i -= 1
            print(f'извините вы ввели не математическую операцию, начните заново у вас осталось {i} попыток')
        else:
            try:
                e = float(input('введите  третье число'))  # теперь проверяем третье число
            except ValueError:
                i -= 1
                print(f'это не число, введите, число. у вас осталось {i} попыток')
            else:
                i = 0
                if oper == '/':
                    if b == 0:
                        print('извините, деление на ноль не возможно') # в случае деления, проверяем что бы делитель в скобках не был = 0
                    else:
                        res = a / b  # выполянем операцию в скобках деление
                        if oper2 == '/':
                            if e == 0:
                                print('извините, деление на ноль не возможно') # в случае деления, проверяем что бы делитель за скобками не был = 0
                            else:
                                result = res / e  # выполянем операцию после скобок
                                print(result)
                        elif oper2 == '+':
                            result = res + e
                            print(result)
                        elif oper2 == '-':
                            result = res - e
                            print(result)
                        elif oper2 == '*':
                            result = res * e
                            print(result)
                elif oper == '+':  # выполянем операцию в скобках сумма
                    res = a + b
                    if oper2 == '/':  # в случае деления, проверяем что бы делитель за скобками не был = 0
                        if e == 0:
                            print('извините, деление на ноль не возможно')
                        else:
                            result = res / e  # выполянем операцию после скобок
                            print(result)
                    elif oper2 == '+':
                        result = res + e
                        print(result)
                    elif oper2 == '-':
                        result = res - e
                        print(result)
                    elif oper2 == '*':
                        result = res * e
                        print(result)
                elif oper == '-':  # выполянем операцию в скобках вычитание
                    res = a - b
                    if oper2 == '/':
                        if e == 0:
                            print('извините, деление на ноль не возможно')  # в случае деления, проверяем что бы делитель за скобками не был = 0
                        else:
                            result = res / e  # выполянем операцию после скобок
                            print(result)
                    elif oper2 == '+':
                        result = res + e
                        print(result)
                    elif oper2 == '-':
                        result = res - e
                        print(result)
                    elif oper2 == '*':
                        result = res * e
                        print(result)
                elif oper == '*':  # выполянем операцию в скобках умножение
                    res = a * b
                    if oper2 == '/':
                        if e == 0:
                            print('извините, деление на ноль не возможно')
                        else:
                            result = res / e  # выполянем операцию после скобок
                            print(result)
                    elif oper2 == '+':
                        result = res + e
                        print(result)
                    elif oper2 == '-':
                        result = res - e
                        print(result)
                    elif oper2 == '*':
                        result = res * e
                        print(result)