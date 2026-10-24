alphabet = "abcdefghijklmnopqrstuvwxyz"

first_half_with_start_and_end_indices = alphabet[0:13]
print(first_half_with_start_and_end_indices)


first_half_with_end_index = alphabet[:13]
print(first_half_with_end_index)


second_half_with_start_and_end_indices = alphabet[13:26]
print(second_half_with_start_and_end_indices)


second_half_with_end_index = alphabet[13:]
print(second_half_with_end_index)


every_second_letter = alphabet[::2]
print(every_second_letter)


reverse_word = alphabet[::-1]
print(reverse_word)


every_third_letter_in_reverse = alphabet[::-3]
print(every_third_letter_in_reverse)