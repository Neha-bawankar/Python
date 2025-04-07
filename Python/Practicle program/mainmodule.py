# main.py
import mymodule  # Importing the module

# Using the functions from the module
name = "Neha"
print(mymodule.greet(name))  # Output: Hello, Neha!

num1, num2 = 10, 5
print(f"The sum of {num1} and {num2} is: {mymodule.add(num1, num2)}")  # Output: 15
print(f"The difference between {num1} and {num2} is: {mymodule.subtract(num1, num2)}")  # Output: 5

