# Task One
number_tuple = (2,5,6,9,10,4)

new_tuple = number_tuple + (7,)

print(new_tuple)



# Task Two
numbers = (1, 2, [3,4], 5)

numbers[2][1] = 99

print(numbers)



# Task Three
tuple_of_fruits = ("apple","banana","cherry")
print(tuple_of_fruits)

list_of_fruits = list(tuple_of_fruits)
print(list_of_fruits)

list_of_fruits += ["mango"]
print(list_of_fruits)

list_of_fruits = tuple(list_of_fruits)
print(list_of_fruits)



# Task Four
a, b, *others = (10, 20, 30, 40)
print (a)
print(b)
print(others)



# Task Five
def sum_of_elements_in_list(number_list):
	for outer_list_index in range(len(number_list)):
		sum_of_numbers = 0

		for number in number_list[outer_list_index]:
			sum_of_numbers += number
		number_list[outer_list_index] = sum_of_numbers

	return number_list

number_list = [[2,3,4],[1,5,7],[4,6,8],[5,6,7]]
print(sum_of_elements_in_list(number_list))



# Task Six
def sum_of_elements_with_same_index(number_list):
	new_list = []
	for checker in range(len(number_list[0])):
		sum_of_numbers = 0

		for outer_list_index in range(len(number_list)):

			sum_of_numbers += number_list[outer_list_index][checker]
		new_list.append(sum_of_numbers)

	return new_list

number_list = [[2,3,4],[1,5,7],[4,6,8],[5,6,7]]
print(sum_of_elements_with_same_index(number_list))



# Task Seven
number_list = list(range (1,21))

def is_even(number):
	return number % 2 == 0

even_number_list = list(filter(is_even, number_list))
print(even_number_list)



# Task Eight
word_list = ["cat","elephant","tiger","lion"]

def is_longer_than_five_letters(word):
	return len(word) > 5 

new_list = list(filter(is_longer_than_five_letters,word_list))
print(new_list)



# Task Nine
def is_number_greater_than_two(number_list):
	return number_list[0] > 2


tuple_list = [(1,'A'), (4, 'B'), (2, 'C')]

new_tuple_list = list(filter(is_number_greater_than_two, tuple_list))
print(new_tuple_list)



# Task Ten
list_of_numbers = list(range(1, 51))

def is_divisible_by_five_and_three(number):
	return number % 3 == 0 and number % 5 == 0


new_number_list = list(filter(is_divisible_by_five_and_three, list_of_numbers))
print(new_number_list)



# Task Eleven
word_list = ["level","world","madam","python"]

def is_palindrome(word):
	return word[::-1] == word

palindrome_list = list(filter(is_palindrome, word_list))
print(palindrome_list)



# Task Twelve
word_list = ["python","java","c++"]

def to_upper_case(word):
	return word.upper()

upper_case_list = list(map(to_upper_case, word_list))
print(upper_case_list)



# Task Thirteen
number_list = list(range(1,11))

def square_of(number):
	return number ** 2

squared_list = list(map(square_of, number_list))
print(squared_list)



# Task Fourteen
names = ["john", "mary", "steve"]

def capitalize_first_letter(word):
	return word.capitalize()

new_list = list(map(capitalize_first_letter, names))
print(new_list)



# Task Fifteen
prices = [100, 200, 300]

def add_tax(number):
	tax = 0.1 * number
	return number + tax

taxed_list = list(map(add_tax, prices))
print(taxed_list)



# Task Sixteen
from functools import reduce

list_of_numbers = list(range(1,51))

def sum_of_numbers(accumulator, number):
	return accumulator + number

summed_list = reduce(sum_of_numbers, list_of_numbers)
print(summed_list)



# Task Seventeen
numbers = [3, 5, 9, 2, 8]

def get_maximum(accumulator, number):
	largest = number
	if accumulator > largest:
		return accumulator
	else:
		return largest

maximum_number = reduce(get_maximum, numbers)
print(maximum_number)



# Task Eighteen
words = ["I","love","Python"]

def concatenate_words(accumulator, word):
	return accumulator + " " + word

sentence = reduce(concatenate_words, words)
print(sentence)



# Task Nineteen
numbers = [1,2,3,4]

def product_of(accumulator, number):
	return accumulator * number

def square_of(number):
	return number ** 2

product = reduce(product_of, numbers)
print(product)

square_list = list(map(square_of, numbers))
print(square_list)



# Task Twenty 
list_of_tuples = [(1, 2),(3, 4),(5, 6)]

def sum_of_numbers(number):
	return number[0] + number[1]

summed_list = list(map(sum_of_numbers, list_of_tuples))

def is_greater_than_5(number):
	return number > 5

final_list = list(filter(is_greater_than_5, summed_list))
print(final_list)



# Task Twenty - One
data = ['123','456','789','abc','def']

def is_number(element):		
	return element.isdigit()

number_list = list(filter(is_number, data))

def sum_of_numbers(numbers):
	total = 0

	for element in numbers:
		total += int(element)
	return total

summed_list = list(map(sum_of_numbers, number_list))
print(summed_list)




















