principal = 1000
rate = 0.07

for years in range (1,31):
	amount_after_years = principal * (1 + rate) ** years
	print(f"The amount of money you'll have after {years} years is ${amount_after_years:.2f}")
