def summarize_letters(word):
	word_list = []
	checked_letters = []

	for outerloop in range(len(word)):
		count = 1
		if word[outerloop].isalpha():
			if word[outerloop].lower() in checked_letters:
				continue

			for innerloop in range(outerloop + 1, len(word)):
			 
				if word[outerloop].lower() == word[innerloop].lower():
					count += 1
		
			checked_letters.append(word[outerloop].lower())

			if count > 1:
				tuple_of_duplicate = (word[outerloop].lower(),count)

				word_list.append(tuple_of_duplicate)

	return word_list

word = "AccoMmodatem,,"

print(summarize_letters(word))	