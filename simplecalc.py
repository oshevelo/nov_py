from conv import conv
def simplecalc(a,c):
	try:
		c=int(c)
		r=conv(a)
		for i in range (c):
			d=input('Введите действие (+ or - or * or /): ')
			b=input('Введите второе число: ')
			b=conv(b)	
			if d=='+':
				r+=b
			elif d=='-':
				r-=b
			elif d=='*':
				r*=b
			elif d=='/':
				r/=b
			else:
				print ('Неправильное действие: ')
		print(r)
		print ('До свидания!')
		input()
	except TypeError :
		print('Неправильное значение: ')
	except ValueError:
		print('Неправильное значение: ')
	except ZeroDivisionError:
		print ('На 0 делить нельзя: ')