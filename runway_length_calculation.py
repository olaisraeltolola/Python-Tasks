speed = float(input("Enter the speed in meters/second: "))
acceleration = float(input("Enter the acceleration in meters/second squared: "))

runway_length = speed**2/(2*acceleration)
print("The minimum runway length =", runway_length)