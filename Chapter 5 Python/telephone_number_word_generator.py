phone_map = {
		"2": "ABC",
		"3": "DEF",
		"4": "GHI",
		"5": "JKL",
		"6": "MNO",
		"7": "PRS",
		"8": "TUV",
		"9": "WXY"
}


phone_number = input("Please enter a phone number: ")

combinations = [""]


for digit in phone_number:
	if digit ==  


for digit in phone_number:
	new_combinations = []

	
	for combination in combinations:

		for letter in phone_map[digit]:
			new_combination = combination + letter
			new_combinations.append(new_combination)


	combinations = new_combinations



print("Total combinations:",len(combinations))