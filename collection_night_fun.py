students = [
	("Alice", 78),
	("Bob", 45),	
	("Charlie", 90),
	("Diana", 62),
	("Kent", 30)
]



# Task One
for student, score in students:
	print(f"{student} => {score}")
print()



# Task Two
print("Students that scored above 60 include: ", end = "")

for student, score in students:
	if score >= 60:
		print(student, end = ", ")
print()



# Task Three
count = 0

for student, score in students:
	if score >= 50:
		count += 1

print (f"{count} students passed")
print()
print()





products = [
	("Laptop", 1200),
	("Mouse", 25),
	("Keyboard", 45),
	("Monitor", 300),
	("USB Cable", 10)
]


# Task One
def is_greater_than_100(product):
	return product[1] > 100

new_list = list(filter(is_greater_than_100, products))
print(new_list)



# Task Two
from functools import reduce 

def get_costs(cost):
	return cost[1]

cost_list = list(map(get_costs, products))

def sum_up_costs(accumulator, costs):
	return accumulator + costs


total_amount = reduce(sum_up_costs, cost_list)
print(total_amount)



# Task Three
for product, cost in products:
	print(f"Product: {product} - Price: {cost}")






points = [ 
	(2, 3),
	(-1, 4),
	(5, -6),
	(0, 7),
	(-3, -2),
]
	

# Task One	
def get_positive_points(point):
	first_point, second_point = point

	return first_point > 0 and second_point > 0

positive_points = list(filter(get_positive_points, points))
print(positive_points)






employees = [
	("John","IT",50000),
	("Jane","HR",45000),
	("Mike","IT",60000),
	("Sara","Finance",70000)
]



# Task One
for name, department, salary in employees:
	print(f"Name: {name} Department: {department}	Salary: {salary}")



# Task Two
def is_IT_employee(employee):
	return employee[1] == "IT"	

IT_employees = list(filter(is_IT_employee, employees))

def is_salary_greater_than_55000(salary):
	return salary[2] > 55000

final_list = list(filter(is_salary_greater_than_55000, IT_employees))
print(final_list)









