driving_distance = float(input("Enter the driving distance: "))
fuel_efficiency = float(input("Enter the miles per gallon: "))
price_per_gallon = float(input("Enter the price per gallon: "))

cost_of_trip = price_per_gallon * (driving_distance/fuel_efficiency)

print("The cost of driving is $", cost_of_trip, sep="")