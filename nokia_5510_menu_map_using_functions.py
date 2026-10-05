menu_choice = ""

def display_menu():
	return """ 


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
	
	




def phonebook_menu():
	return """

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

def phonebook_menu_options():

	phonebook_choice = input(phonebook_menu()).lower()

	match(phonebook_choice):
		case "0": print("Going back"); main_menu()
		case "home": print("Welcome back"); main_menu()
		case "1": print("--Search--"); phonebook_menu_options() 
		case "2": print("--Service Nos.--"); phonebook_menu_options()
		case "3": print("--Add name--"); phonebook_menu_options()
		case "4": print("--Erase--"); phonebook_menu_options()
		case "5": print("--Edit--"); phonebook_menu_options()

		case "6": print("--Copy--"); phonebook_menu_options()
		case "7": print("--Assign Tone--"); phonebook_menu_options()
		case "8": print("--Send b'card--"); phonebook_menu_options()
		case "10": print("--Speed dials--"); phonebook_menu_options()
		case "11": print("--Voice Tag--"); phonebook_menu_options()
		case "9": options_menu()

		case _: print("Invalid choice, please choose again"); phonebook_menu()


def options():
	return """

--OPTIONS--
Press

1. Memory in use
2. Type of view
3. Memory status
Home: To go to the main menu

0. Back
"""

def options_menu():
	options_choice = input(options()).lower()

	match(options_choice):
		case "home": main_menu()
		case "0": phonebook_menu_options()
		case "1": print("--Memory in use--"); options_menu() 
		case "2": print("--Type of view--"); options_menu()
		case "3": print("--Memory status--"); options_menu()
		case _: print("Invalid choice, please choose again"); options_menu()








def message_menu():

	return """

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

def message_menu_options():
	message_menu_choice = input(message_menu()).lower()

	match(message_menu_choice):

		case "home": print("Welcome back"); main_menu()
		case "0": print("Going back"); main_menu()				
		case "1": print("--Write messages--"); message_menu_options()
		case "2": print("--Inbox--"); message_menu_options()
		case "3": print("--Outbox--"); message_menu_options()
		case "4": print("--Picture messages--"); message_menu_options()
		case "5": print("--Templates--"); message_menu_options()
		case "6": print("--Smileys--"); message_menu_options()
		case "8": print("--Info service--"); message_menu_options()
		case "9": print("--Voice mailbox number--"); message_menu_options()
		case "10": print("--Serve command editor--"); message_menu_options()

		case "7": message_settings_menu_options()


def message_settings_menu():
	return """

--MESSAGE SETTINGS--
Press

1. Set 1
2. Common
Home: To go to the main menu

0. Back
"""


def set_1_menu():

	return """

--SET 1--
Press

1. Message centre number
2. Messages sent as
3. Message validity
Home: To go to the main menu

0. Back

"""

def common_menu():
	return """

--COMMON--
Press
 
1. Delivery reports
2. Reply via same centre
3. Character support
Home: To go to the main menu

0. Back
"""

def message_settings_menu_options():
	message_settings_menu_choice = input(message_settings_menu()).lower()

	match(message_settings_menu_choice):
		case "home": main_menu()
		case "0": message_menu_options()

		case "1": set_1_options()
		case "2": common_options()
		case _: print("Invalid choice, please choose again"); message_settings_menu_options()


def set_1_options():
	set_1_choice = input(set_1_menu()).lower()

	match(set_1_choice):
		case "home": main_menu()
		case "0": message_settings_menu_options()
		case "1": print("--Message centre number--"); set_1_options()
		case "2": print("--Messages sent as--"); set_1_options()
		case "3": print("--Message validity--"); set_1_options()
		case _: print("Invalid choice, please choose again"); set_1_options()


def common_options():
	common_choice = input(common_menu()).lower()

	match(common_choice):
		case "home": main_menu()
		case "0": message_settings_menu_options()
		case "1": print("--Delivery reports--"); common_options()
		case "2": print("--Reply via same centre--"); common_options()
		case "3": print("--Character support--"); common_options()
		case _: print("Invalid choice, please choose again"); common_options() 






def call_register_menu():
	return """

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

def call_register_menu_options():

	call_register_menu_choice = input(call_register_menu()).lower()

	match(call_register_menu_choice):
		case "home": main_menu()
		case "0": main_menu()				
		case "1": print("--Missed calls--"); call_register_menu_options()
		case "2": print("--Received calls--"); call_register_menu_options()
		case "3": print("--Dialled numbers--"); call_register_menu_options()
		case "4": print("--Erase recent call lists--"); call_register_menu_options()
		case "8": print("--Prepaid credit--"); call_register_menu_options()
		case "5": call_duration_menu_options()
		case "6": call_costs_menu_options()
		case "7": call_cost_settings_menu_options()
		case _: print("Invalid choice, please choose again"); call_register_menu_options() 



def call_duration_menu():
	return """

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

def call_duration_menu_options():

	call_duration_menu_choice = input(call_duration_menu()).lower()

	match(call_duration_menu_choice):
		case "home": main_menu()
		case "0": call_register_menu_options()
		case "1": print("--Last call duration--"); call_duration_menu_options()
		case "2": print("--All calls' duration--"); call_duration_menu_options()
		case "3": print("--Received calls' duration--"); call_duration_menu_options()
		case "4": print("--Dialled calls' duration--"); call_duration_menu_options()
		case "5": print("--Clear timers--"); call_duration_menu_options()
		case _: print("Invalid choice, please choose again"); call_duration_menu_options() 

def call_costs_menu():
	return """

--CALL COSTS--
Press
1. Last call cost
2. All calls' cost
3. Clear counters
Home: To go to the main menu

0. Back

"""

def call_costs_menu_options():
	call_costs_menu_choice = input(call_costs_menu()).lower()

	match(call_costs_menu_choice):
		case "home": main_menu()
		case "0": call_register_menu_options()
		case "1": print("--Last call cost--"); call_costs_menu_options()
		case "2": print("--All calls' cost--"); call_costs_menu_options()
		case "3": print("--Clear counters--"); call_costs_menu_options()
		case _: print("Invalid choice, please choose again"); call_costs_menu_options() 
	
def call_cost_settings_menu():
	return """

--CALL COST SETTINGS--
Press
1. Call cost limit
2. Show costs in
Home: To go to the main menu

0. Back

"""

def call_cost_settings_menu_options():
	call_costs_settings_menu_choice = input(call_cost_settings_menu()).lower()

	match(call_costs_settings_menu_choice):
		case "home": main_menu()
		case "0": call_register_menu_options()
		case "1": print("--Call cost limit--"); call_cost_settings_menu_options()
		case "2": print("--Show costs in--"); call_cost_settings_menu_options()
		case _: print("Invalid choice, please choose again"); call_cost_settings_menu_options()





def tones_menu():
	return """

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

def tones_menu_options():
	tones_menu_choice = input(tones_menu()).lower()

	match(tones_menu_choice):
		case "home": main_menu()
		case "0": main_menu()				
		case "1": print("--Ringing tone--"); tones_menu_options()
		case "2": print("--Ringing volume--"); tones_menu_options()
		case "3": print("--Incoming call alert--"); tones_menu_options()
		case "4": print("--Message alert tone--"); tones_menu_options()
		case "5": print("--Keypad tones--"); tones_menu_options()
		case "6": print("--Warning tones--"); tones_menu_options()
		case "7": print("--Vibrating alert--"); tones_menu_options()
		case "8": print("--Screen saver--"); tones_menu_options()
		case _: print("Invalid choice, please choose again"); tones_menu_options()






def settings_menu():
	return """

--SETTINGS--
Press

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
Home: To go to the main menu

0. Back
"""

def settings_menu_options():
	settings_menu_choice = input(settings_menu()).lower()

	match(settings_menu_choice):
		case "home": main_menu()
		case "0": main_menu()				
		case "4": print("--Restore factory settings--"); settings_menu_options()
		case "1": call_settings_menu_options()
		case "2": phone_settings_menu_options()
		case "3": security_settings_menu_options()
		case _: print("Invalid choice, please choose again"); settings_menu_options()


def call_settings_menu():
	return """

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


def call_settings_menu_options():
	call_settings_menu_choice = input(call_settings_menu()).lower()

	match(call_settings_menu_choice):
		case "home": main_menu()
		case "0": settings_menu_options()
		case "1": print("--Automatic redial--"); call_settings_menu_options()
		case "2": print("--Speed dialling--"); call_settings_menu_options()
		case "3": print("--Call waiting options--"); call_settings_menu_options()
		case "4": print("--Own number sending--"); call_settings_menu_options()
		case "5": print("--Phone line in use--"); call_settings_menu_options()
		case "6": print("--Automatic answer--"); call_settings_menu_options()
		case _: print("Invalid choice, please choose again"); call_settings_menu_options() 


def phone_settings_menu():
	return """

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

def phone_settings_menu_options():
				
	phone_settings_menu_choice = input(phone_settings_menu()).lower()

	match(phone_settings_menu_choice):
		case "home": main_menu()
		case "0": settings_menu_options()
		case "1": print("--Language--"); phone_settings_menu_options()
		case "2": print("--Cell info display--"); phone_settings_menu_options()
		case "3": print("--Welcome note--"); phone_settings_menu_options()
		case "4": print("--Network selection--"); phone_settings_menu_options()
		case "5": print("--Confirm SIM Service actions--"); phone_settings_menu_options()
		case _: print("Invalid choice, please choose again"); phone_settings_menu_options()


def security_settings_menu():
	return """

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

def security_settings_menu_options():
	security_settings_menu_choice = input(security_settings_menu()).lower()

	match(security_settings_menu_choice):
		case "home": main_menu()
		case "0": settings_menu_options()
		case "1": print("--PIN code request--"); security_settings_menu_options()
		case "2": print("--Call barring service--"); security_settings_menu_options()
		case "3": print("--Fixed dialling--"); security_settings_menu_options()
		case "4": print("--Closed user group--"); security_settings_menu_options()
		case "5": print("--Security level--"); security_settings_menu_options()
		case "6": print("--Change access codes--"); security_settings_menu_options()
		case _: print("Invalid choice, please choose again"); security_settings_menu_options() 





def music_menu():
	return """

--MUSIC--
Press

1. Music player
2. Radio
3. Recorder
4. Track list
Home: To go to the main menu

0. Back

"""

def music_menu_options():
	music_menu_choice = input(music_menu()).lower()	

	match(music_menu_choice):
		case "home": main_menu()
		case "0": main_menu()				
		case "1": print("--Music player--"); music_menu_options()
		case "2": print("--Radio--"); music_menu_options()
		case "3": print("--Recorder--"); music_menu_options()
		case "4": print("--Track list--"); music_menu_options()
		case _: print("Invalid choice, please choose again"); music_menu_options()


def clock_menu():
	return """

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

def clock_menu_options():
	clock_menu_choice = input(clock_menu()).lower()

	match(clock_menu_choice):
		case "home": main_menu()
		case "0": main_menu()	
		case "1": print("--Alarm clock--"); clock_menu_options()
		case "2": print("--Clock settings--"); clock_menu_options()
		case "3": print("--Date setting--"); clock_menu_options()
		case "4": print("--Stopwatch--"); clock_menu_options()
		case "5": print("--Countdown timer--"); clock_menu_options()
		case "6": print("--Auto update of date and time--"); clock_menu_options()
		case _: print("Invalid choice, please choose again"); clock_menu_options()



def main_menu():
	menu_choice = input(display_menu())

	match(menu_choice):
		case "0": print("Turning off...")
		case "1": phonebook_menu_options()
		case "2": message_menu_options()
		case "3": print("Welcome to Chat"); main_menu()
		case "4": call_register_menu_options()
		case "5": tones_menu_options()
		case "6": settings_menu_options()
		case "7": print("Welcome to Call divert"); main_menu()
		case "8": music_menu_options()
		case "9": print("Welcome to Games"); main_menu()
		case "10": print("Welcome to Calculator"); main_menu()
		case "11": print("Welcome to Reminders"); main_menu()
		case "12": clock_menu_options()
		case "13":print("Welcome to Profiles"); main_menu()
		case "14":print("Welcome to Services"); main_menu()
		case "15":print("Welcome to SIM Services"); main_menu()
		case _: print("Invalid choice, please choose again"); main_menu()


		

main_menu()
