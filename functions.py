def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

def is_prime_number(number):
	counter = 0
	for index in range(2,number):
		if number % index == 0:
			counter += 1

	if counter == 0 and number > 1:
		return True
	else:
		return False

def subtract_two_numbers(number_one, number_two):
	if number_one > number_two:
		return number_one - number_two
	else:
		return number_two - number_one


def divide_two_numbers(number_one,number_two):
	if number_two != 0:
		return number_one/number_two
	else:
		return 0.0



def factor_of(number):
	counter = 0
	for index in range(1,number + 1):
		if number % index == 0:
			counter += 1

	return counter


def is_square(number):
	if number % number ** 0.5 == 0:
		return True
	else:
		return False


def is_palindrome(number):
	digit_one = number // 10000
	digit_two = (number // 1000) % 10
	digit_four = (number // 10) % 10
	digit_five = number % 10

	if digit_one == digit_five and digit_two == digit_four:
		return True
	else:
		return False


def factorial_of(number):
	factorial = 1
	for index in range(number, 0, -1):
		factorial *= index
	return factorial

def square_of_number(number):
	return number ** 2


print(is_even(5))
print(is_prime_number(1))
print(subtract_two_numbers(3,1))
print(divide_two_numbers(0,9))
print(factor_of(10))
print(is_square(26))
print(is_palindrome(262))
print(factorial_of(7))
print(square_of_number(4))

