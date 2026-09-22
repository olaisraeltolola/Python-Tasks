repeat = True

skip_level = "0"
skip_nested_level = "0"
first_back_option = "0"
second_back_option = "0"
third_back_option = "0"
fourth_back_option = "0"

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

	menu_choice = "0"
	if(skip_level == "0"):
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

			skip_level = "0"
			functions_under_phonebook_menu = "0"
			if first_back_option == "0":
				functions_under_phonebook_menu = input(phonebook_menu).lower()
			else:
				functions_under_phonebook_menu = first_back_option
			match(functions_under_phonebook_menu):

				case "0": print("Going back")
				case "home": print("Welcome back")
				case "1": print("--Search--"); repeat = False
				case "2": print("--Service Nos.--");repeat = False
				case "3": print("--Add name--");repeat = False
				case "4": print("--Erase--");repeat = False
				case "5": print("--Edit--");repeat = False
				case "6": print("--Copy--");repeat = False
				case "7": print("--Assign Tone--");repeat = False
				case "8": print("--Send b'card--");repeat = False
				case "10": print("--Speed dials--");repeat = False
				case "11": print("--Voice Tag--");repeat = False

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
					first_back_option = "0"
					functions_under_options = input(options_menu).lower()
	
					match(functions_under_options):
						case "home": print("Welcome back")
						case "0": skip_level = "1"
						case "1": print("--Memory in use--");repeat = False
						case "2": print("--Type of view--");repeat = False
						case "3": print("--Memory status--");repeat = False
						case _: print("Invalid choice, please choose again"); first_back_option = "9"; skip_level = "1"


				case _: print("Invalid choice, please choose again"); skip_level = "1"

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
Home: To go to the main menu

0. Back

"""
			skip_level = "0"
			functions_under_message_menu = "0"
			if (skip_nested_level == "0"):
				functions_under_message_menu = input(message_menu).lower()
			else:
				functions_under_message_menu = skip_nested_level

			match(functions_under_message_menu):

				case "home": print("Welcome back")
				case "0": print("Going back")				
				case "1": print("--Write messages--");repeat = False
				case "2": print("--Inbox--");repeat = False
				case "3": print("--Outbox--");repeat = False
				case "4": print("--Picture messages--");repeat = False
				case "5": print("--Templates--");repeat = False
				case "6": print("--Smileys--");repeat = False
				case "8": print("--Info service--");repeat = False
				case "9": print("--Voice mailbox number--");repeat = False
				case "10": print("--Serve command editor--");repeat = False

				case "7":
					message_settings_menu = """

--MESSAGE SETTINGS--
Press

1. Set 1
2. Common
Home: To go to the main menu

0. Back
"""
					skip_nested_level = "0"
					if second_back_option == "0":
						options_under_message_settings_menu = input(message_settings_menu).lower()
					else:
						options_under_message_settings_menu = second_back_option
					match(options_under_message_settings_menu):
						case "home": print("Welcome back")

						case "0": skip_level = "2"

						case "1":
							options_under_set_1 = """

--SET 1--
Press

1. Message centre number
2. Messages sent as
3. Message validity
Home: To go to the main menu

0. Back

"""
							second_back_option = "0"
							functions_under_set_1 = input(options_under_set_1).lower()

							match(functions_under_set_1):
								case "home": print("Welcome back")
								case "0":skip_nested_level = "7"; skip_level = "2"
								case "1": print("--Message centre number--");repeat = False
								case "2": print("--Messages sent as--");repeat = False
								case "3": print("--Message validity--");repeat = False
								case _: print("Invalid choice, please choose again"); second_back_option = "1"; skip_nested_level = "7"; skip_level = "2"


						case "2":

							options_under_common = """

--COMMON--
Press
 
1. Delivery reports
2. Reply via same centre
3. Character support
Home: To go to the main menu

0. Back
"""
							second_back_option = "0"						
							functions_under_common = input(options_under_common).lower()

							match(functions_under_common):
								case "home": print("Welcome back")
								case "0": skip_nested_level = "7"; skip_level = "2"
								case "1": print("--Delivery reports--");repeat = False
								case "2": print("--Reply via same centre--");repeat = False
								case "3": print("--Character support--");repeat = False
								case _: print("Invalid choice, please choose again"); second_back_option = "2"; skip_nested_level = "7"; skip_level = "2"


						case _: print("Invalid choice, please choose again"); skip_nested_level = "7"; skip_level = "2"


				case _: print("Invalid choice, please choose again"); skip_level = "2"



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
Home: To go to the main menu

0. Back

"""
			skip_level = "0"
			if third_back_option == "0":
				functions_under_call_register_menu = input(call_register_menu).lower()
			else:
				functions_under_call_register_menu = third_back_option

			match(functions_under_call_register_menu):
				case "home": print("Welcome back")
				case "0": print("Going back")				
				case "1": print("--Missed calls--");repeat = False
				case "2": print("--Received calls--");repeat = False
				case "3": print("--Dialled numbers--");repeat = False
				case "4": print("--Erase recent call lists--");repeat = False
				case "8": print("--Prepaid credit--");repeat = False
			

				case "5":
					options_under_call_duration = """

--CALL DURATION--
Press
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
Home: To go to the main menu

0. Back

"""
					third_back_option = "0"

					functions_under_call_duration = input(options_under_call_duration).lower()

					match(functions_under_call_duration):
						case "home": print("Welcome back")
						case "0": skip_level = "4"
						case "1": print("--Last call duration--");repeat = False
						case "2": print("--All calls' duration--");repeat = False
						case "3": print("--Received calls' duration--");repeat = False
						case "4": print("--Dialled calls' duration--");repeat = False
						case "5": print("--Clear timers--");repeat = False
						case _: print("Invalid choice, please choose again"); third_back_option = "5"; skip_level = "4"


				case "6":
					options_under_call_costs = """

--CALL COSTS--
Press
1. Last call cost
2. All calls' cost
3. Clear counters
Home: To go to the main menu

0. Back

"""
					third_back_option = "0"

					functions_under_call_costs = input(options_under_call_costs).lower()

					match(functions_under_call_costs):
						case "home": print("Welcome back")
						case "0": skip_level = "4"
						case "1": print("--Last call cost--");repeat = False
						case "2": print("--All calls' cost--");repeat = False
						case "3": print("--Clear counters--");repeat = False
						case _: print("Invalid choice, please choose again"); third_back_option = "6"; skip_level = "4"


				case "7":
					options_under_call_cost_settings = """

--CALL COST SETTINGS--
Press
1. Call cost limit
2. Show costs in
Home: To go to the main menu

0. Back

"""
					third_back_option = "0"

					functions_under_call_cost_settings = input(options_under_call_cost_settings).lower()

					match(functions_under_call_cost_settings):
						case "home": print("Welcome back")
						case "0": skip_level = "4"
						case "1": print("--Call cost limit--");repeat = False
						case "2": print("--Show costs in--");repeat = False
						case _: print("Invalid choice, please choose again"); third_back_option = "7"; skip_level = "4"


				case _: print("Invalid choice, please choose again"); skip_level = "4"


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
Home: To go to the main menu

0. Back

"""
			options_under_tones = input(tones_menu).lower()

			match(options_under_tones):
				case "home": print("Welcome back")
				case "0": print("Going back")				
				case "1": print("--Ringing tone--");repeat = False
				case "2": print("--Ringing volume--");repeat = False
				case "3": print("--Incoming call alert--");repeat = False
				case "4": print("--Message alert tone--");repeat = False
				case "5": print("--Keypad tones--");repeat = False
				case "6": print("--Warning tones--");repeat = False
				case "7": print("--Vibrating alert--");repeat = False
				case "8": print("--Screen saver--");repeat = False
				case _: print("Invalid choice, please choose again"); skip_level = "5"
				

		case "6":
			settings_menu = """

--SETTINGS--
Press

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
Home: To go to the main menu

0. Back
"""

			skip_level = "0"
			if fourth_back_option == "0":
				functions_under_settings_menu = input(settings_menu).lower()
			else:
				functions_under_settings_menu = fourth_back_option

			match(functions_under_settings_menu):
				case "home": print("Welcome back")
				case "0": print("Going back")				
				case "4": print("--Restore factory settings--");repeat = False
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
Home: To go to the main menu

0. Back

"""
					fourth_back_option = "0"
					functions_under_call_settings = input(options_under_call_settings).lower()

					match(functions_under_call_settings):
						case "home": print("Welcome back")
						case "0": skip_level = "6"
						case "1": print("--Automatic redial--");repeat = False
						case "2": print("--Speed dialling--");repeat = False
						case "3": print("--Call waiting options--");repeat = False
						case "4": print("--Own number sending--");repeat = False
						case "5": print("--Phone line in use--");repeat = False
						case "6": print("--Automatic answer--");repeat = False
						case _: print("Invalid choice, please choose again"); fourth_back_option = "1"; skip_level = "6"


				case "2":
					options_under_phone_settings = """

--PHONE SETTINGS--
Press

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
Home: To go to the main menu

0. Back

"""
					fourth_back_option = "0"
					functions_under_phone_settings = input(options_under_phone_settings).lower()

					match(functions_under_phone_settings):
						case "home": print("Welcome back")
						case "0": skip_level = "6"
						case "1": print("--Language--");repeat = False
						case "2": print("--Cell info display--");repeat = False
						case "3": print("--Welcome note--");repeat = False
						case "4": print("--Network selection--");repeat = False
						case "5": print("--Confirm SIM Service actions--");repeat = False
						case _: print("Invalid choice, please choose again"); fourth_back_option = "2"; skip_level = "6"



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
Home: To go to the main menu

0. Back
"""
					fourth_back_option = "0"
					functions_under_security_settings = input(options_under_security_settings).lower()

					match(functions_under_security_settings):
						case "home": print("Welcome back")
						case "0": skip_level = "6"
						case "1": print("--PIN code request--");repeat = False
						case "2": print("--Call barring service--");repeat = False
						case "3": print("--Fixed dialling--");repeat = False
						case "4": print("--Closed user group--");repeat = False
						case "5": print("--Security level--");repeat = False
						case "6": print("--Change access codes--");repeat = False
						case _: print("Invalid choice, please choose again"); fourth_back_option = "3"; skip_level = "6"



				case _: print("Invalid choice, please choose again"); skip_level = "6"



		case "7": print("Welcome to Call divert"); repeat = False
		case "8":
			music_menu = """

--MUSIC--
Press

1. Music player
2. Radio
3. Recorder
4. Track list
Home: To go to the main menu

0. Back

"""
			options_under_music = input(music_menu).lower()	

			match(options_under_music):
				case "home": print("Welcome back")
				case "0": print("Going back")				
				case "1": print("--Music player--");repeat = False
				case "2": print("--Radio--");repeat = False
				case "3": print("--Recorder--");repeat = False
				case "4": print("--Track list--");repeat = False
				case _: print("Invalid choice, please choose again"); skip_level = "8"
				


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
Home: To go to the main menu

0. Back

"""
			skip_level = "0"
			options_under_clock = input(clock_menu).lower()

			match(options_under_clock):
				case "home": print("Welcome back")
				case "0": print("Going back")	
				case "1": print("--Alarm clock--");repeat = False
				case "2": print("--Clock settings--");repeat = False
				case "3": print("--Date setting--");repeat = False
				case "4": print("--Stopwatch--");repeat = False
				case "5": print("--Countdown timer--");repeat = False
				case "6": print("--Auto update of date and time--");repeat = False
				case _: print("Invalid choice, please choose again"); skip_level = "12"


		case "13":print("Welcome to Profiles"); repeat = False

		case "14":print("Welcome to Services"); repeat = False

		case "15":print("Welcome to SIM Services"); repeat = False

		case _: print("Invalid choice, please choose again")



