from conv import conv
from datecalc import date_check, date_calc
from datetime import datetime
from simplecalc import simplecalc
print ('3.14=pi, 2.17=e')
print ("Для калькулятора дат используйте формат: YYYY-MM-DD")
c=input('Введите количество действий: ')
a=input('Введите первое число: ')
flag=date_check(a)
if flag==(False):
	simplecalc(a,c)
else:
	date_calc(a,c)
