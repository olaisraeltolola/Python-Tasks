primes = [True] * 1000

for index in range(2,len(primes)):
	for counter in range(index + 1, len(primes)):
		if primes[index] == True:
			if counter % index == 0:
				primes[counter] = False


for list_index, value in enumerate(primes):
	if list_index > 1 and value == True:
		print(f"Index -> {list_index}	Value -> {value}")