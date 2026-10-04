import random

def tortoise_actual_move():
	number = random.randrange(1,11)
	if 1 <= number <= 5:
		return 3

	elif 6 <= number <= 7:
		return -6

	elif 8 <= number <= 10:
		return 1


def hare_actual_move():
	number = random.randrange(1,11)
	if 1 <= number <= 2:
		return 0 
 
	elif 3 <= number <= 4:
		return 9

	elif number == 5:
		return -12

	elif 6 <= number <= 8:
		return 1

	elif 9 <= number <= 10:
		return -2


print("""
BANG !!!!!
AND THEY'RE OFF !!!!!
"""
)

position_of_tortoise = 1
position_of_hare = 1



while True:
	position_of_tortoise += tortoise_actual_move() 
	position_of_hare += hare_actual_move() 

	if position_of_tortoise < 1:
		position_of_tortoise = 1
	if position_of_hare < 1:
		position_of_hare = 1

	for position in range (1,71):
		if position == position_of_tortoise and position == position_of_hare:
			print("OUCH!!!",end="")

		elif position == position_of_tortoise:
			print("T",end="")

		elif position == position_of_hare:
			print("H",end="")
		else:
			print(" ",end="")
	
	print()

	if position_of_tortoise >= 70 and position_of_hare >= 70:
		print("It's a tie. But I favour the tortoise")
		break
	elif position_of_tortoise >= 70:
		print("TORTOISE WINS!!! YAY!!!")
		break
	elif position_of_hare >= 70:
		print("Hare wins. Yuch")
		break
