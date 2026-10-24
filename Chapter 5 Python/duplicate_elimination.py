def get_unique_values(element_list):
	unique_list = []

	for outerloop in range(len(element_list)):
		count = 0

		for innerloop in range(outerloop+1, len(element_list)):

			if element_list[outerloop] == element_list[innerloop]:
				count += 1

		if count == 0:
			unique_list.append(element_list[outerloop])

	return sorted(unique_list)


number_list = [3,6,2,2,3,6,8,5,78,2,2]
print(get_unique_values(number_list))