weight_in_kilograms = float(input("Enter your weight (in kilograms): "))
height_in_meters = float(input("Enter your height (in meters): "))

bmi = (weight_in_kilograms)/((height_in_meters)*(height_in_meters))

if (bmi < 18.5):
	print("Underweight")
elif (bmi >= 18.5 and bmi <= 24.9):
	print("Normal")
elif (bmi >= 25 and bmi <= 29.9):
	print("Overweight")
else: print("Obese")
