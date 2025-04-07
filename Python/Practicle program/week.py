# List of days in a week
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Take user input
day_number = int(input("Enter a number between 1 and 7: "))

# Check if the input is valid
if 1 <= day_number <= 7:
    # Print the corresponding day
    print("The day of the week is:", days_of_week[day_number - 1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")