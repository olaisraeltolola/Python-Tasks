def fahrenheit(temperature):
	fahrenheit = ((9/5) * temperature) + 32
	return fahrenheit

print("Celsius	Fahrenheit")

for temperature in range (0,101):

	print (f"{temperature:.1f}	{fahrenheit(temperature):.1f}")