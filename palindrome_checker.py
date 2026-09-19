word = input("Enter a 3-letter word: ")
length = len(word)

first_letter = word[0]
second_letter = word[1]
third_letter = word[2]

if first_letter == third_letter and length == 3:
	print("This word is a palindrome")

if first_letter != third_letter and length == 3:
	print("This word is not a palindrome")

elif length > 3:
	print("This is not a 3-letter word")
