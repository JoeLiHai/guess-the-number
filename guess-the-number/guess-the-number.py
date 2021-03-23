import random
start = int(input('Please decide the start of the range: '))
end = int(input('Please decide the end of the range: '))
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('Please enter an integer: ')
	num = int(num)
	if num == r:
		print('You got the right number!')
		print('This is the' , count, 'th time you guessed')
		break
	elif num > r:
		print('The number you guess is bigger than the answer.')
	elif num < r:
		print('The number tou guess is smaller than the answer')
	print('This is the' , count, 'th time you guessed')



