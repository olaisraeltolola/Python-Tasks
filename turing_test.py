first_prompt = input("What is your problem? ")
second_prompt = input("Have you had this problem before? (yes or no)\n").lower()

if second_prompt == "yes":
	print("Well, you have it again")
else: 
	print("Well you have it now")