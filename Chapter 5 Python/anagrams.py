def get_anagrams(word):
	if len(word) == 1:
		return [word]

	
	list_of_anagrams = []

	for index in range(len(word)):
		first_letter = word[index]

		remaining_letters = word[:index] + word[index + 1:]

		other_anagrams = get_anagrams(remaining_letters)

		for anagram in other_anagrams:
			new_anagram = first_letter + anagram
		
			list_of_anagrams.append(new_anagram)


	return list_of_anagrams

print(get_anagrams("dogs"))
			