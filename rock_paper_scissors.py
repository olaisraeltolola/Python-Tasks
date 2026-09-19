player_one = input("Player one move: ").casefold()
player_two = input("Player two move: ").casefold()

first_move = "rock"
second_move = "paper"
third_move = "scissors"

if (player_one == first_move):

	if (player_two == second_move):
		print("Player Two wins!")
	else:
		if (player_two == third_move):
			print("Player One wins!")
		else: print("Tie!")
              
else:
	if (player_one == second_move):

		if (player_two == first_move):
			print("Player One wins!")
		else:
			if (player_two == third_move):
				print("Player Two wins!")
			else: print("Tie!")

	else:
		if (player_one == third_move):
		
			if (player_two == first_move):
				print("Player Two wins!")
			else:
				if (player_two == second_move):
					print("Player One wins!")
				else: print("Tie!")
