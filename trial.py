repeat = True

skip_print = 0
back_option = 0

while (repeat):
	menu_functions = """ 


Welcome to the Nokia 5510 phone

To access any of the menu functions: 

Press 

1. Phonebook
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM Services 


 """

	menu_choice = 0
	if(skip_print == 0):
		menu_choice = int(input(menu_functions))
	else:
		menu_choice = skip_print
		
	match(menu_choice):
		case 1:
			phonebook_menu = """

--PHONEBOOK--
Press

1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign Tone
8. Send b'card
9. Options
10. Speed dials
11. Voice tags 

0. Back

"""

			skip_print = 0
			functions_under_phonebook_menu = int(input(phonebook_menu))

			match(functions_under_phonebook_menu):
				case 1: repeat = False
				case 2: repeat = False
				case 3: repeat = False
				case 4: repeat = False
				case 5: repeat = False
				case 6: repeat = False
				case 7: repeat = False
				case 8: repeat = False
				case 10: repeat = False
				case 11: repeat = False
