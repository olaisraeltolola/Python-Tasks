number = int(input("Enter the number of rows for your triangle: "))

for counter in range (number):
	print (f"{'*' * (counter + 1): <{number}} {'*' * (number - counter): <{number}} {(' ' * (counter + 1)) + ('*' * (number - counter)): <{number}} {(' ' * (number - counter)) + ('*' * (counter + 1)): <{number}}")