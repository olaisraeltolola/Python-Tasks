for counter in range (5):

	temperature_in_celsius = float(input("Enter a temperature in celsius: "))

	temperature_in_fahrenheit = (temperature_in_celsius *(9/5)) + 32

	if (temperature_in_celsius <= -273):
		print("Impossible!")

	else:
		print("Celsius to Fahrenheit = (",temperature_in_celsius,"x (9/5)) + 32 =",temperature_in_fahrenheit)