# get user input for two variables
a = input("Enter value for variable a: ")
b = input("Enter value for variable b: ")

print("Before swap:")
print("a =", a)
print("b =", b)

# swap the values using a temporary variable
temp = a
a = b
b = temp

print("After swap:")
print("a =", a)
print("b =", b)