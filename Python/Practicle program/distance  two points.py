import math

def calculate_distance():
    x1 = float(input("Enter x-coordinate of point 1: "))
    y1 = float(input("Enter y-coordinate of point 1: "))
    x2 = float(input("Enter x-coordinate of point 2: "))
    y2 = float(input("Enter y-coordinate of point 2: "))

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print(f"The distance between the two points is: {distance:.2f}")

calculate_distance()