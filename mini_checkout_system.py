name = input("Enter your name: ")
sum_of_price_of_products = 0
price = 0

while(True):

	product_name = input("Enter the product name: ")
	quantity = int)input(f"Enter the quantity of {product_name}: "))

	price_of_product = float(input(f"Enter the price of {product_name}: "))
	total_price = price_of_product * quantity_of_product
	sum_of_price_of_products += total_price
	
	
	enquiry = input("Do you want to purchase another product: ").lower()

	match(enquiry):
		case "no": break;
		case "yes": True;
		case _:	print("It is a yes or no question oga")

if enquiry == "no":
	print(f"Thank you {name} for patronizing our services")
	print(f"Your bill is {sum_of_price_of_products:,.2f}")

