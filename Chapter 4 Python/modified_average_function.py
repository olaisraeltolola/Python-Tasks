def average(number, *numbers):
	return (sum(numbers) + number)/(len(numbers) + 1)

print(average(3,4,5,6,7))