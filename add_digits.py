number = input("Please enter a number: ")

def add_digits(number):
	length_of_number = len(number);

	if length_of_number == 1:
		return number

	else:
	
		sum_of_digits = 0;

		for index in range (length_of_number):
			digit = int(number[index]) - int('0')
			sum_of_digits += digit

		string_sum_of_digits = str(sum_of_digits)

		return add_digits(string_sum_of_digits)

print(add_digits(number))


