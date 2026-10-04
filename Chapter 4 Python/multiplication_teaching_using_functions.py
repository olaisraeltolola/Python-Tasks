import random

def numbers_generate():
	digit_one = random.randrange(1,10)
	digit_two = random.randrange(1,10)

	return digit_one,digit_two

result = numbers_generate()

number_one = result[0]
number_two = result[1]

while True:
	answer = int(input(f"How much is {number_one} times {number_two}\n"))

	if answer == (number_one * number_two):
		print("Very good!")
		break

	else:
		print("No. Please try again")