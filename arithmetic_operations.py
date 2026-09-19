number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

sum = number_one + number_two + number_three
average = sum/3
product = number_one * number_two * number_three
smallest = min(number_one, number_two, number_three) 
largest = max(number_one, number_two, number_three) 

print("The sum is", sum)
print("The average is", average)
print("The product is", product)
print("The smallest number is", smallest)
print("The largest number is", largest)