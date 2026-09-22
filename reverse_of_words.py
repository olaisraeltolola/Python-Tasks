word = input("Enter a word: ")
reverse_word = ""

index_of_word = (len(word) - 1)


for index in range(index_of_word, -1, -1):
	reverse_word += word[index]
print(reverse_word)


