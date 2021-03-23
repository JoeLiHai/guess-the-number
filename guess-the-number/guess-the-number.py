import random

r = random.randint(1, 100)
while True:
	num = input('Please enter an integer: ')
	num = int(num)
	if num == r:
		print('You got the right number!')
		break
	elif num > r:
		print('The number you guess is bigger than the answer.')
	elif num < r:
		print('The number tou guess is smaller than the answer')



