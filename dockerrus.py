import time



while True:
	a = int(input('Введи первое число: '));
	b = int(input('Введи второе число: '));
	c = input('Введи что нужно с ним сделать?: ');

	if c == '+':
		print (a+b);
	elif c == '-':
		print (a-b);
	elif c == '*':
		print (a*b);
	else:
		print (a/b);
	time.sleep(1)


