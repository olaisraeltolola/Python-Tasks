word = input("Please enter a word: ")

def get_number_from_letter(word):
	phone_number = ""

	phone_map = {
			"A": "2", "B": "2", "C": "2", 
			"D": "3", "E": "3", "F": "3", 
			"G": "4", "H": "4", "I": "4", 
			"J": "5", "K": "5", "L": "5", 
			"M": "6", "N": "6", "O": "6", 
			"P": "7", "R": "7", "S": "7",
			"T": "8", "U": "8", "V": "8", 
			"W": "9", "X": "9", "Y": "9", 

}

	for letter in word.upper():
		phone_number += phone_map[letter]

	return phone_number


print(get_number_from_letter(word))