 #Importing the array module
from array import array

# Create an array of two numbers
numbers = array('i', [10, 20])  # 'i' represents an array of integers

# Display the array
print("Array elements:", numbers[0], numbers[1])

# Access and print individual elements
print("First number:", numbers[0])
print("Second number:", numbers[1])

# Perform an operation (e.g., sum of the two numbers)
sum_of_numbers = numbers[0] + numbers[1]
print("Sum of the two numbers:", sum_of_numbers)