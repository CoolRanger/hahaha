
def determine(word):
	a = int(word[0])
	b = int(word[1])
	c = int(word[2])
	if b - a == c - b:
		return 'a'
	elif b / a == c / b:
		return 'b'
	else:
		return 'c'
word = input('請輸入一等差或等比數列').split()
result = determine(word)
if result == 'a':
			print('此為等差數列')
elif result == 'b':
			print('此為等比數列')
else:	
			print('叫你輸入等差或等比數列,別搞')






