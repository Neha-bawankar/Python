# Dictionary of months and their corresponding number of days
days_in_month = {
    "January": 31,
    "February": 28,  # Assuming it's not a leap year
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Take user input
month = input("Enter the name of the month: ").capitalize()

# Check if the input is valid
if month in days_in_month:
    # Print the corresponding number of days
    print(f"{month} has {days_in_month[month]} days.")
else:
    print("Invalid month name! Please enter a correct month name.")