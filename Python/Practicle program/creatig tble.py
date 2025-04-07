from tabulate import tabulate

# Data for the table
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]

# Creating the table
table = tabulate(data, headers="firstrow", tablefmt="grid")

# Display the table
print("Advanced Table:")
print(table)