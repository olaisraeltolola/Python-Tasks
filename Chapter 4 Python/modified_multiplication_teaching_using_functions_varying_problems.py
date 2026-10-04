import random

def multiplication():

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


def addition():

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
		answer = int(input(f"What is {number_one} + {number_two}\n"))
	
		if answer == (number_one + number_two):
			print(correct_responses_generate())
			break

		else:
			print(incorrect_responses_generate())




def subtraction():

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
		answer = int(input(f"What is {number_one} - {number_two}\n"))
	
		if answer == (number_one - number_two):
			print(correct_responses_generate())
			break

		else:
			print(incorrect_responses_generate())


def division():

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
		answer = float(input(f"What is {number_one} divided by {number_two}\n"))

		correct_answer = float(f"{number_one/number_two:.2f}")
	
		if answer == correct_answer:
			print(correct_responses_generate())
			break

		else:
			print(incorrect_responses_generate())

def random_mixture():
	problem = random.randrange(1,5)

	match (problem):
		case 1: return addition()
		case 2: return subtraction()
		case 3: return multiplication()
		case 4: return division()	




problem_type = int(input("""
Please enter:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Random Mixture of Problems
\n"""))

match (problem_type):
	case 1: addition()

	case 2: subtraction()

	case 3: multiplication()

	case 4: division()

	case 5: random_mixture()
		


