import random
def level_one():

	def numbers_generate():	
		digit_one = random.randrange(1,10)
		digit_two = random.randrange(1,10)
	
		return digit_one,digit_two


	result = numbers_generate()

	number_one = result[0]
	number_two = result[1]

	def correct_responses_generate():
		correct_response = random.randrange(1,4)
	
		match(correct_response):
			case 1: return "Very good!"
			case 2: return "Nice work!"
			case 3: return "Keep up the good work!"

	def incorrect_responses_generate():
		incorrect_response = random.randrange(1,4)
	
		match(incorrect_response):
			case 1: return "No. Please try again."
			case 2: return "Wrong. Try once more."
			case 3: return "No. Keep trying."


	while True:
		answer = int(input(f"How much is {number_one} times {number_two}\n"))

		if answer == (number_one * number_two):
			print(correct_responses_generate())
			break

		else:
			print(incorrect_responses_generate())


def level_two():

	def numbers_generate():	
		number_one = random.randrange(1,100)
		number_two = random.randrange(1,100)
	
		return number_one, number_two

	result = numbers_generate()
	
	number_one = result[0]
	number_two = result[1]

	def correct_responses_generate():
		correct_response = random.randrange(1,4)
	
		match(correct_response):
			case 1: return "Very good!"
			case 2: return "Nice work!"
			case 3: return "Keep up the good work!"

	def incorrect_responses_generate():
		incorrect_response = random.randrange(1,4)
	
		match(incorrect_response):
			case 1: return "No. Please try again."
			case 2: return "Wrong. Try once more."
			case 3: return "No. Keep trying."


	while True:
		answer = int(input(f"How much is {number_one} times {number_two}\n"))
	
		if answer == (number_one * number_two):
			print(correct_responses_generate())
			break

		else:
			print(incorrect_responses_generate())


difficulty_level = int(input("Please enter a difficulty level (1 or 2)\n"))

match (difficulty_level):
	case 1: level_one()


	case 2: level_two()
		


