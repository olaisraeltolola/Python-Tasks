def is_palindrome(word):
	reverse_word = ""
	for index in range(-1, (-len(word)) - 1, -1):
		if word[index].isalpha():
			reverse_word += word[index]
	print(reverse_word)

	new_word = ""
	for second_index in range(len(word)):
		if word[second_index].isalpha():
			new_word += word[second_index]
	print(new_word)

	return reverse_word == new_word

word = input("Please enter a word: ").lower()

print(is_palindrome(word))
		
