title = "Multiplication Table"
print (f"{title:>40}")

for numbers in range (1,10):
	print(f"	{numbers:>2}",end="")
print()

for border in range (74):
	print("-",end="")
print()

for row in range (1,10):
	print(f"{row}  |",end="")

	for column in range (1,10):
		print (f"\t{row * column:>2}",end="")
	
	print()

	