word = input("Enter a word: ")

length = len(word)

if length < 5:
	print("Short string")
if 5 <= length <= 10:
	print("Medium string")
if length > 10:
	print("Long string")

