number = int(input("Enter a 5-digit number: "))
index = 10000

for digit_picker in range(5):
	digit = (number // index) 
	number = number % index
	index = index // 10

	print(digit,end="\t")