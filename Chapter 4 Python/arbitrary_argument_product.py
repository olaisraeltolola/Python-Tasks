def product_of_numbers(*numbers):
	product = 1
	for number in numbers:
		product *= number
	return product


print(product_of_numbers(2,3,5,6))
print(product_of_numbers(2,3,5,6,5,4,3,2))
print(product_of_numbers(2,3,5))