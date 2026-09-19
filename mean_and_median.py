number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))
number_four = int(input("Enter the fourth number: "))

largest = 0
second_largest = 0
smaller = 0
smallest = 0

if number_two > number_one > number_three > number_four:
	largest = number_two
	second_largest = number_one
	smaller = number_three
	smallest = number_four

elif number_two > number_one > number_four > number_three:
	largest = number_two
	second_largest = number_one
	smaller = number_four
	smallest = number_three

elif number_two > number_three > number_four > number_one:
	largest = number_two
	second_largest = number_three
	smaller = number_four
	smallest = number_one

elif number_two > number_three > number_one > number_four:
	largest = number_two
	second_largest = number_three
	smaller = number_one
	smallest = number_four

elif number_two > number_four > number_three > number_one:
	largest = number_two
	second_largest = number_four
	smaller = number_three
	smallest = number_one

elif number_two > number_four > number_one > number_three:
	largest = number_two
	second_largest = number_four
	smaller = number_one
	smallest = number_three




elif number_one > number_two > number_three > number_four:
	largest = number_one
	second_largest = number_two
	smaller = number_three
	smallest = number_four

elif number_one > number_two > number_four > number_three:
	largest = number_one
	second_largest = number_two
	smaller = number_four
	smallest = number_three

elif number_one > number_three > number_two > number_four:
	largest = number_one
	second_largest = number_three
	smaller = number_two
	smallest = number_four

elif number_one > number_three > number_four > number_two:
	largest = number_one
	second_largest = number_three
	smaller = number_four
	smallest = number_two

elif number_one > number_four > number_two > number_three:
	largest = number_one
	second_largest = number_four
	smaller = number_two
	smallest = number_three

elif number_one > number_four > number_three > number_two:
	largest = number_one
	second_largest = number_four
	smaller = number_three
	smallest = number_two




elif number_three > number_one > number_two > number_four:
	largest = number_three
	second_largest = number_one
	smaller = number_two
	smallest = number_four

elif number_three > number_one > number_four > number_two:
	largest = number_three
	second_largest = number_one
	smaller = number_four
	smallest = number_two

elif number_three > number_two > number_four > number_one:
	largest = number_three
	second_largest = number_two
	smaller = number_four
	smallest = number_one

elif number_three > number_two > number_one > number_four:
	largest = number_three
	second_largest = number_two
	smaller = number_one
	smallest = number_four

elif number_three > number_four > number_one > number_two:
	largest = number_three
	second_largest = number_four
	smaller = number_one
	smallest = number_two

elif number_three > number_four > number_two > number_one:
	largest = number_three
	second_largest = number_four
	smaller = number_two
	smallest = number_one



elif number_four > number_one > number_two > number_three:
	largest = number_four
	second_largest = number_one
	smaller = number_two
	smallest = number_three

elif number_four > number_one > number_three > number_two:
	largest = number_four
	second_largest = number_one
	smaller = number_three
	smallest = number_two

elif number_four > number_two > number_one > number_three:
	largest = number_four
	second_largest = number_two
	smaller = number_one
	smallest = number_three

elif number_four > number_two > number_three > number_one:
	largest = number_four
	second_largest = number_two
	smaller = number_three
	smallest = number_one

elif number_four > number_three > number_one > number_two:
	largest = number_four
	second_largest = number_three
	smaller = number_one
	smallest = number_two

elif number_four > number_three > number_two > number_one:
	largest = number_four
	second_largest = number_three
	smaller = number_two
	smallest = number_one


median = (second_largest + smaller)/2

sum_of_numbers = number_one + number_two + number_three + number_four

mean = (sum_of_numbers)/4

print(f"The median = {median}")
print(f"The sum = {sum_of_numbers}")
print(f"The mean = {mean}")










