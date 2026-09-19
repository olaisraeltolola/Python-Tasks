number_of_correct = 0
number_of_wrong = 0
for counter in range (5):

	number_one = int(input("Enter the first number: "))
	number_two = int(input("Enter the second number: "))
	operator = input("Enter the mathematical sign: ")

	print("Question: ",number_one, operator, number_two)

	correct_answer = 0

	match(operator):

		case'+': correct_answer = number_one + number_two;

		case'-': correct_answer = number_one - number_two;

		case'x': correct_answer = number_one * number_two;

		case'/': correct_answer = number_one / number_two;

	answer = float(input("Answer: "))

	if correct_answer == answer:
		print("You are correct")
		number_of_correct += 1

	else:
		print("You are wrong")
		number_of_wrong += 1

print("The number of correct answers = ",number_of_correct)
print("The number of wrong answers = ",number_of_wrong)


	
