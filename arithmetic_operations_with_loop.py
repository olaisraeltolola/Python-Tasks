sum_of_numbers = 0
product = 1
average = 0.0
largest_number = 0
for counter in range(4):
	number = int(input("Enter a number: "))
	smallest_number = number
	sum_of_numbers += number
	product *= number

	if largest_number < number:
		largest_number = number
	if smallest_number > number:
		smallest_number = number

average = sum_of_numbers/4

print("Sum =", sum_of_numbers)
print("Product =", product)
print("Average =", average)
print("Largest number =", largest_number)
print("Smallest number =", smallest_number)
