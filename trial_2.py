repeat = True

skip_level = 0
skip_nested_level = 0
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
0. Turn off

"""

	menu_choice = 0
	if(skip_level == 0):
		menu_choice = input(menu_functions)
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

			skip_level = 0
			back_option = 0
			if (back_option == 0):
				functions_under_phonebook_menu = input(phonebook_menu).lower()
			else:
				back_option = functions_under_phonebook_menu

			match(functions_under_phonebook_menu):

				case "home": print("Welcome back")
				case "0": print("You are going back")
				case "1": print("--Search--"); repeat = False
				case "2": print("--Service Nos.--");repeat = False
				case "3": print("--Add name--");repeat = False
				case "4": print("--Erase--");repeat = False
				case "5": print("--Edit--");repeat = False
				case "6": print("--Copy--");repeat = False
				case "7": print("--Assign Tone--");repeat = False
				case "8": print("--Send b'card--");repeat = False
				case "10": print("--Speed dials--");repeat = False
				case "11": print("--Voice Tags--");repeat = False

				case "9":
					options_menu = """

--OPTIONS--
Press

1. Memory in use
2. Type of view
3. Memory status 
 
Home: To go to the main menu
0. Back
"""
					
					functions_under_options = input(options_menu)
					match(functions_under_options):
						case "0": skip_level = 1
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False
						case _:  back_option = 9; print("Invalid choice, please choose again")

				case _: skip_level = 1; print("Invalid choice, please choose again"); 



		case "2":
			message_menu = """

--MESSAGES--
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

0. Back

"""
			skip_level = 0
			functions_under_message_menu = 0
			if (skip_nested_level == 0):
				functions_under_message_menu = input(message_menu)
			else:
				functions_under_message_menu = skip_nested_level

			match(functions_under_message_menu):
				
				case "1": repeat = False
				case "2": repeat = False
				case "3": repeat = False
				case "4": repeat = False
				case "5": repeat = False
				case "6": repeat = False
				case "8": repeat = False
				case "9": repeat = False
				case "10": repeat = False

				case "7":
					message_settings_menu = """

--MESSAGE SETTINGS--
Press

1. Set 1
2. Common

0. Back
"""
					skip_nested_level = 0
					options_under_message_settings_menu = input(message_settings_menu)

					match(options_under_message_settings_menu):
						case "0": skip_level = 2

						case "1":
							options_under_set_1 = """

--SET 1--
Press

1. Message centre number
2. Messages sent as
3. Message validity

0. Back

"""
							functions_under_set_1 = input(options_under_set_1)

							match(functions_under_set_1):
								case "0":skip_nested_level = 7; skip_level = 2
								case "1": repeat = False
								case "2": repeat = False
								case "3": repeat = False


						case "2":
							options_under_common = """

--COMMON--
Press
 
1. Delivery reports
2. Reply via same centre
3. Character support

0. Back
"""
							functions_under_common = input(options_under_common)

							match(functions_under_common):
								case "0": skip_nested_level = 7; skip_level = 2
								case "1": repeat = False
								case "2": repeat = False
								case "3": repeat = False




		case "3": print("Welcome to Chat"); repeat = False


		case "4":
			call_register_menu = """

--CALL REGISTER--
Press

1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit

0. Back

"""
			skip_level = 0
			functions_under_call_register_menu = input(call_register_menu)

			match(functions_under_call_register_menu):
				case "1": repeat = False
				case "2": repeat = False
				case "3": repeat = False
				case "4": repeat = False
				case "8": repeat = False
			

				case "5":
					options_under_call_duration = """

--CALL DURATION--
Press
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers

0. Back

"""
					functions_under_call_duration = input(options_under_call_duration)

					match(functions_under_call_duration):
						case "0": skip_level = 4
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False
						case "4": repeat = False
						case "5": repeat = False


				case "6":
					options_under_call_costs = """

--CALL COSTS--
Press
1. Last call cost
2. All calls' cost
3. Clear counters

0. Back

"""
					functions_under_call_costs = input(options_under_call_costs)

					match(functions_under_call_costs):
						case "0": skip_level = 4
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False

				case "7":
					options_under_call_cost_settings = """

--CALL COST SETTINGS--
Press
1. Call cost limit
2. Show costs in

0. Back

"""
					functions_under_call_cost_settings = input(options_under_call_cost_settings)

					match(functions_under_call_cost_settings):
						case "0": skip_level = 4
						case "1": repeat = False
						case "2": repeat = False

		case "5":
			tones_menu = """

--TONES--
Press

1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver

0. Back

"""
			options_under_tones = input(tones_menu)

			match(options_under_tones):
				case "1": repeat = False
				case "2": repeat = False
				case "3": repeat = False
				case "4": repeat = False
				case "5": repeat = False
				case "6": repeat = False
				case "8": repeat = False

		case "7":
			settings_menu = """

--SETTINGS--
Press

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings

0. Back
"""

			skip_level = 0
			functions_under_settings_menu = input(settings_menu)

			match(functions_under_settings_menu):
				case "4": repeat = False
				case "1":
					options_under_call_settings = """

--CALL SETTINGS--
Press

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer

0. Back

"""
					functions_under_call_settings = input(options_under_call_settings)

					match(functions_under_call_settings):
						case "0": skip_level = 6
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False
						case "4": repeat = False
						case "5": repeat = False
						case "6": repeat = False


				case "2":
					options_under_phone_settings = """

--PHONE SETTINGS--
Press

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions

0. Back

"""
					functions_under_phone_settings = input(options_under_phone_settings)

					match(functions_under_phone_settings):
						case "0": skipPrint = 6
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False
						case "4": repeat = False
						case "5": repeat = False


				case "3":
					options_under_security_settings = """

--SECURITY SETTINGS--
Press

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes

0. Back
"""
					functions_under_security_settings = input(options_under_security_settings)

					match(functions_under_security_settings):
						case "0": skip_level = 6
						case "1": repeat = False
						case "2": repeat = False
						case "3": repeat = False
						case "4": repeat = False
						case "5": repeat = False
						case "6": repeat = False

		case "7": print("Welcome to Call divert"); repeat = False
		case "8":
			music_menu = """

--MUSIC--
Press

1. Music player
2. Radio
3. Recorder
4. Track list

0. Back

"""
			options_under_music = input(music_menu)	

			match(options_under_music):
				case "1": repeat = False
				case "2": repeat = False
				case "3": repeat = False
				case "4": repeat = False


		case "9": print("Welcome to Games"); repeat = False

		case "10":print("Welcome to Calculator"); repeat = False

		case "11":print("Welcome to Reminders"); repeat = False

		case "12":
			clock_menu = """

--CLOCK--
Press

1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time

0. Back

"""
			options_under_clock = input(clock_menu)

			match(options_under_clock):
				case "1": repeat = False
				case "2": repeat = False
				case "3": repeat = False
				case "4": repeat = False
				case "5": repeat = False
				case "6": repeat = False


		case "13":print("Welcome to Profiles"); repeat = False

		case "14":print("Welcome to Services"); repeat = False

		case "15":print("Welcome to SIM Services"); repeat = False

		case _: print("Invalid choice, please choose again"); repeat = False


