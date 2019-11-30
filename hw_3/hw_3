from lib import foo_input_float  # check input on float
from lib import operations  # dict of available operations
from lib import foo_input_oper  # check on math operations
from lib import foo_date_input  # check date format dd.mm.yyyy
from lib import ask_day_or_calc  # what type of calc user want tu start
from lib import check_date_str
from simpleeval import simple_eval

# 1. with asking
ask = ask_day_or_calc()  # ask what user want to try: 1. calc 2. date calc
if ask == 1:  # calc
    a = foo_input_float('первое число')  # first numb
    oper = foo_input_oper()  # first operation
    b = foo_input_float('второе число')  # second numb
    res = operations[oper](a, b)  # result of first operation
    oper2 = foo_input_oper()  # second operation
    e = foo_input_float('третье число')  # third numb
    res_all = operations[oper2](res,e)  # result
    print(f'({a} {oper} {b}) {oper2} {e} = {res_all}')
else:  # date calc
    f_date = foo_date_input('первую')  # first date
    i = 5
    while i != 0:
        s_date = foo_date_input('вторую')  # second date
        if s_date > f_date:
            i -= 1
            print(f'для вычисления разницы дат, вторая дата должна быть раньше первой, повторите ввод второй даты, осталось {i} попыток')
        else:
            i = 0
            delta = f_date - s_date
            print(f' между {s_date} и {f_date} прошло {delta.days} дней')

# 2. without asking
i = 5
while i != 0:
    user_srt = input('введите выражение (численное или дату в формате: дд.мм.гггг)')
    if check_date_str(user_srt) is not None:  # checking is it a date, if yes start calc dates
        f_date = check_date_str(user_srt)
        s_date = foo_date_input('вторую')  # second date
        if s_date > f_date:
            i -= 1
            print(
                f'для вычисления разницы дат, вторая дата должна быть раньше первой, повторите, осталось {i} попытки')
        else:
            i = 0
            delta = f_date - s_date
            print(f' между {s_date} и {f_date} прошло {delta.days} дней')
    else: # if not date using simple_eval
        try:
            res = simple_eval(user_srt)
            i = 0
            print(f'результат: {res}')
        except:
            i -= 1
            print(f'вы ввели не математическое выражение и не дату, пробуйте еще у вас осталось {i} попыток')
