number_of_day_of_week = int(input("Enter a number between 1 and 7: "))

match (number_of_day_of_week):
	case 1: print("Monday");
	case 2: print("Tuesday");
	case 3: print("Wednesday");
	case 4: print("Thursday");
	case 5: print("Friday");
	case 6: print("Saturday");
	case 7: print("Sunday");
	case _: print("This number is not between 1 and 7")
