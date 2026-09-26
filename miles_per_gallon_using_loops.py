sum_of_miles = 0.0
sum_of_gallons = 0.0
gallons = 0.0

while (gallons != -1):
	gallons = float(input("Enter the gallons used (-1 to end): "))
	sum_of_gallons += gallons
	
	if gallons == -1:
		break

	miles = float(input("Enter the miles driven: "))
	sum_of_miles += miles

	print("The miles/gallon for this tank was",(miles/gallons))


print("The overall average miles/gallon was",(sum_of_miles/(sum_of_gallons + 1)))