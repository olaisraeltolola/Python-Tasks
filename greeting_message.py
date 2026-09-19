name = input("Enter your name: ")
length_of_name = len(name)

if 1 <= length_of_name <= 5:
	print("Hi", name, "!") 

elif length_of_name > 5:
	print("Hello", name, "!") 