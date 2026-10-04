def display_menu():

	return  """ 


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
0. Turn off

"""




while (True):
	
	menu_choice = "0"
	if(skip_level == "0"):
		menu_choice = input(display_menu())
	else:
		menu_choice = skip_level
		
	match(menu_choice):
		case "0": repeat = False
		case "1":
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
Home: To go to the main menu

0. Back

"""

