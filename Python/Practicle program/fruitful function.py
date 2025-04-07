# Defining a fruitful function
def calculate_area(length, width):
    """Function to calculate the area of a rectangle."""
    area = length * width
    return area  # This is a fruitful function because it returns a value

# Main part of the program
if __name__ == "__main__":
    # Taking input from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calling the fruitful function
    area = calculate_area(length, width)

    # Using the returned value
    print(f"The area of the rectangle is: {area}")

