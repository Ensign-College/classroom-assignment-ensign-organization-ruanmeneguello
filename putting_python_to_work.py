import math
#test 2
# TO-DO: get the radius of the circle from the user
try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a number for the radius.")
    exit()

# TO-DO: calculate the diameter of the circle
diameter = 2 * radius

# TO-DO: calculate the circumference of the circle
# Formula: C = 2 * pi * r
circumference = 2 * math.pi * radius

# TO-DO: calculate the area of the circle
# Formula: A = pi * r^2
area = math.pi * (radius ** 2)

# TO-DO: print the values for the user
print("\n--- Circle Calculations ---")
print(f"Radius: {radius:.2f}")
print(f"Diameter: {diameter:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.2f}")
