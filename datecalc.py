from datetime import datetime
def date_check(date_string):
	try:
		datetime.strptime(date_string, "%Y-%m-%d")
		return True
	except ValueError:
		return False
def date_calc (a,c):
	a=datetime.strptime(a, "%Y-%m-%d").date()
	try:
		c=int(c)
		for i in range (c):
			#d=input('Введите действие (-): ')
			b=input('Введите второе число: ')
			b=datetime.strptime(b, "%Y-%m-%d").date()
			r=a-b			
		print(r)
	except ValueError:
		print ('Неправильное значениее второго числа')