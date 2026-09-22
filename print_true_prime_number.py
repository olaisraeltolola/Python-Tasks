number = int(input("Enter a number: "))
end_range = (number // 2) + 1
counter = 0

for index in range (2, end_range):
	if number % index == 0:
		counter += 1

if number <= 1:
	counter += 1

if counter == 0:
	print("True")
else: 
	print("False")