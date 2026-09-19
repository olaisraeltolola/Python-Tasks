letter_one = input("Enter a letter: ").casefold()

try:
	if len(letter_one) != 1 or not letter_one.isalpha():
		raise ValueError

except ValueError:
	print("Invalid input")
	

if (letter_one == "a" or letter_one == "e" or letter_one == "i" or letter_one == "o" or letter_one == "u"):
	print("Vowel")
elif len(letter_one) == 1 and letter_one.isalpha(): print("Consonant")

