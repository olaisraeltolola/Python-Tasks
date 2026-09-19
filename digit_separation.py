number_one = int(input("Enter a five-digit number: "))

num1 = number_one // 10000
num2 = (number_one // 1000) % 10
num3 = (number_one // 100) % 10
num4 = (number_one // 10) % 10
num5 = (number_one % 10)

print(num1, num2, num3, num4, num5, sep="\t")
