# password setup
password = 'a123456'
i = 3
while i > 0 :
	pwd = input('enter your password: ')
	if pwd == password :
		print('congrates, you log in successfully.')
		break
	else:
		i = i - 1
		print('wrong password, you have', i, 'times remaining.')
		

