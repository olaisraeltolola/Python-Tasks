def get_prime_number(number_list):
	prime_list = []

	for list_index in range(len(number_list)):
		count = 0

		for number in range(2,number_list[list_index]):
			if number_list[list_index] % number == 0:
				count += 1


		if count == 0 and number_list[list_index] > 1:
			prime_list.append(number_list[list_index])

	return prime_list



number_list = [3,50,7,9,10,8]

print(get_prime_number(number_list))


def replace_negative_numbers(number_list):
	for list_index in range (len(number_list)):
		if number_list[list_index] < 0:
			number_list[list_index] = 0

	return number_list

second_number_list = [-5,6,-8,0,23,6]

print (replace_negative_numbers(second_number_list))


def move_zeros_to_end_of_list(number_list):
	list_of_zeros = []
	new_list = []

	for list_index in range (len(number_list)):
		if number_list[list_index] == 0:
			list_of_zeros.append(number_list[list_index])
		else:
			new_list.append(number_list[list_index])

	return new_list + list_of_zeros

third_number_list = [5,3,0,2,0,12,7]

print (move_zeros_to_end_of_list(third_number_list))


def get_duplicate_numbers(number_list):

	duplicate_list = []
	for outer_checker in range (len(number_list)):
		for inner_checker in range (outer_checker + 1,len(number_list)):
			if number_list[outer_checker] == number_list[inner_checker]:
				duplicate_list.append(number_list[inner_checker])


	return duplicate_list


fourth_number_list = [45,60,3,0,67,2,45,3,22,0]

print(get_duplicate_numbers(fourth_number_list))

		








