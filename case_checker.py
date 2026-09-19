string = input("Enter a string: ")

if string[0].isupper():
	print("The first letter is uppercase")
elif string[0].islower():
	print("The first letter is lowercase")
else: 
	print("The first character is not a letter")