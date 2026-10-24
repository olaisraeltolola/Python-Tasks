numbers = [
	[0,0,0],
	[0,0,0]
]



counter = 1

for row in range(len(numbers)):
	for column in range(len(numbers[row])):
		numbers[row][column] = counter
		counter += 1
	
print("  0 1 2")

for row in range(len(numbers)):
	print(row, end = " ")
	for column in range(len(numbers[row])):
		print(numbers[row][column], end = " ")
	print()

