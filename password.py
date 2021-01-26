password = 'a123456'
chance = 3
while chance > 0:
	test = input('請輸入密碼')
	if test == 'a123456':
		print('登入成功')
	else:
		print('密碼錯誤，還有', int(chance) - 1 , '次機會')
		chance = int(chance) - 1
raise SystemExit