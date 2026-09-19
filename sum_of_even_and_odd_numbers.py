integers = int(input("How many integers do you want to input? "))

sum_of_even = 0
sum_of_odd = 0
for counter in range(integers):
	number = int(input("Enter a number: "))
	if number % 2 == 0:
		sum_of_even = sum_of_even + number

	if number % 2 != 0:
		sum_of_odd = sum_of_odd + number

print("The sum of even numbers =", sum_of_even)
print("The sum of odd numbers =", sum_of_odd)
