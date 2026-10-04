import random
def play_game():
	number = random.randrange(1,1000)
	guess = ""
	count = 0

	while guess != number:
		guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
		count+=1
				

		if guess > number:
			print("Too high. Try again")
			print()
		elif guess < number:
			print("Too low. Try again")
			print()

		else:
			guess = number
			print("Congratulations! You guessed my number!")

	if count <= 10:
		print("Either you know the secret or you got lucky!")
	elif count > 10:
		print("You should be able to do better!")

response = "yes"
while response != "no":
	play_game()

	response = input("Would you like to play again? ").lower()