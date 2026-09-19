total_bill = float(input("Enter your total bill: "))
membership = input("Are you a member? ")

if (total_bill >= 1000 and membership == "yes"): 
	print("You have 10% off\nYour total bill is", (total_bill-(total_bill * 0.1)))

elif (total_bill >= 1000 and membership == "no"):
	print("You have 5% off\nYour total bill is", (total_bill-(total_bill * 0.05)))

else: print("You have no discount, your final amount is", total_bill)