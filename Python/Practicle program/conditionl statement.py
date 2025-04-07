# If Statement
number = int(input('Enter a number: '))

# check if number is greater than 0
if number > 0:
    print(f'{number} is a positive number.')

print('A statement outside the if statement.')


#If-else Statement
number = int(input('Enter a number: '))

if number > 10:
    print('Positive number')
else:
    print('Not a positive number')

print('This statement always executes')

#if -elif-else
number = int(input('Enter a number: '))


if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')


#nested -if statement
number = int(input("enter the value of number"))

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')