import random
def play_game():
	number = random.randrange(1,1000)
	guess = ""


	while guess != number:
		guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
		
		if guess > number:
			print("Too high. Try again")
			print()
		elif guess < number:
			print("Too low. Try again")
			print()

		else:
			guess = number
			print("Congratulations! You guessed my number!")

response = "yes"
while response != "no":
	play_game()

	response = input("Would you like to play again? ").lower()