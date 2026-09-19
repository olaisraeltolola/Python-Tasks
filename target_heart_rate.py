age = int(input("Enter your age: "))
maximum_heart_rate = 220 - age
target_heart_range_min = 0.5 * maximum_heart_rate
target_heart_range_max = 0.85 * maximum_heart_rate

print("Your maximum heart rate is", maximum_heart_rate)
print("The range of your target heart rate is", target_heart_range_min, "-", target_heart_range_max)

