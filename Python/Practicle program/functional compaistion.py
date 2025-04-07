def compose(f, g):
    return lambda x: f(g(x))

# Example functions
def square(x):
    return x * x

def add_five(x):
    return x + 5

# Get user input
num = int(input("Enter a number: "))

# Composing functions
# First add five to the number, then square the result
composed_function = compose(square, add_five)

# Applying the composed function to the user input
result = composed_function(num)

# Output the result
print(f"The result of applying the composed function is: {result}")

