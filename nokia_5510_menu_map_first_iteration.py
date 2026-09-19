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



menu_choice = int(input(menu_functions))

		
match(menu_choice):
	case 1: 
		phonebook_menu = """

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


"""


		functions_under_phonebook_menu = int(input(phonebook_menu))

		match(functions_under_phonebook_menu):
			case 9: 
				options_menu = """

Press

1. Memory in use
2. Type of view
3. Memory status  

"""

				print(options_menu)




	case 2: 
		message_menu = """

Press 

1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Serve command editor
		
"""

		functions_under_message_menu = int(input(message_menu))

		match(functions_under_message_menu):
			case 7: 
				message_settings_menu = """

Press

1. Set 1
2. Common

"""

				options_under_message_settings_menu = int(input(message_settings_menu))

				match(options_under_message_settings_menu):
					case 1: 
						options_under_set_1 = """

Press

1. Message centre number
2. Messages sent as
3. Message validity

"""

						print(options_under_set_1)


					case 2: 
						options_under_common = """

Press
 
1. Delivery reports
2. Reply via same centre
3. Character support

"""

						print(options_under_common)




	case 3: print("Welcome to Chat")


	case 4: 
		call_register_menu = """

Press

1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit

"""

		functions_under_call_register_menu = int(input(call_register_menu))

		match(functions_under_call_register_menu):
			case 5: 
				options_under_call_duration = """

Press

1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers

"""

				print(options_under_call_duration)		

			case 6: 
				options_under_call_costs = """

Press

1. Last call cost
2. All calls' cost
3. Clear counters

"""

				print(options_under_call_costs)		


			case 7: 
				options_under_call_cost_settings = """

Press

1. Call cost limit
2. Show costs in

"""

				print(options_under_call_cost_settings)	

	
	case 5: 
		tones_menu = """

Press

1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver

"""

		print(tones_menu)	



	case 6: 
		settings_menu = """

Press

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings

"""

		functions_under_settings_menu = int(input(settings_menu))

		match(functions_under_settings_menu):
			case 1: 
				options_under_call_settings = """

Press

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer

"""

				print(options_under_call_settings)	



			case 2: 
				options_under_phone_settings = """

Press

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions

"""

				print(options_under_phone_settings)	



			case 3: 
				options_under_security_settings = """

Press

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes

"""	

				print(options_under_security_settings)	

	case 7: print("Welcome to Call divert")

	case 8: 
		music_menu = """

Press

1. Music player
2. Radio
3. Recorder
4. Track list

"""

		print(music_menu)	


	case 9: print("Welcome to Games")

	case 10: print("Welcome to Calculator")

	case 11: print("Welcome to Reminders")

	case 12: 
		clock_menu = """

Press

1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time

"""

		print(clock_menu)	


	case 13: print("Welcome to Profiles")

	case 14: print("Welcome to Services")

	case 15: print("Welcome to SIM Services")

