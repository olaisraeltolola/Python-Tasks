def sort_in_ascending_order(item_list):
	for outerloop in range(len(item_list)):
		for innerloop in range(outerloop + 1, len(item_list)):
			if item_list[outerloop] > item_list[innerloop]:
				temporary = item_list[outerloop]
				item_list[outerloop] = item_list[innerloop]
				item_list[innerloop] = temporary

	return item_list



def sort_word_in_ascending_order(word):
	word = list(word)
	
	for outerloop in range(len(word)):
		for innerloop in range(outerloop + 1, len(word)):
			if word[outerloop] > word[innerloop]:
				temporary = word[outerloop]
				word[outerloop] = word[innerloop]
				word[innerloop] = temporary

	return "".join(word)



def is_ordered(unordered_iterable):
	if type(unordered_iterable) == list or type(unordered_iterable) == tuple:
		return unordered_iterable == sort_in_ascending_order(unordered_iterable.copy())

	else: 
		return unordered_iterable == sort_word_in_ascending_order(unordered_iterable)
 



number_list = [2,3,4,5,6,10]
word = "hello"

print(is_ordered(word))
print(sort_word_in_ascending_order(word))
