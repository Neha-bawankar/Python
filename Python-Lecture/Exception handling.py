#1 ZeroDivision Error - Raised when division or modulo zero takes for numeric type
'''num1 = 10
num2 = 0
result = num1/num2
print(result)
print("Rest of the code")'''
import time

# Ex -1 Single line error
'''num1 = int(input('Enter the first number'))
num2 = int(input('Enter the first number'))
try:
    div = num1/num2
    print(di)
except ZeroDivisionError:
    print("Divide by zero is not possible")
except NameError:
    print("Name is not available")
print("Rest of the code")'''

#Method 2 Multiple line error
'''num1 = int(input('Enter the first number'))
num2 = int(input('Enter the first number'))
try:
    div = num1/num2
    #Nmae error
   # print(di)
    print(div)

except (Exception) as obj:
    print(obj)

print("rest of the code")'''

#Method-3 Printing exception in output
'''num1 = int(input('ENTER FIRST NUMBER: '))
num2 = int(input("ENTER THE SECOND NUMBER:"))
try:
    div = num1/num2
    print(div)
except Exception as obj:
    print(obj)
    #if i want to check the class exception
    print(obj.__class__)
print("Rest of code")
'''
#Method -4 Sys module
'''import sys
num1 = int(input('ENTER FIRST NUMBER: '))
num2 = int(input("ENTER THE SECOND NUMBER"))
try:
    div = num1/num2
    print(div)
except:
    print(sys.exc_info()[1]) # Zerodivision error

'''
#else block
'''num1 = int(input('enter the fisrt number'))
num2 = int(input("Enter the second number"))
try:
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Division by  zero is not possible")
else:
    print("No exception will occur")
finally:
    print('Always exceute code')
'''











''''
#2 Type Error
int1 = 100
in2 = "String"
result = int1+in2
print(result)'''
'''
# =1 raise exception
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError
    print("Your age is : " , age)
except ValueError:
    print('Enter valid age')
print("rest of code")

# 2 raise exception ex
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Invalid age")
    print("Your age is : " , age)
except ValueError as vars:
   print(vars)
print("rest of code")


#userdefined exception
#ex-1 write a  program for fivedivisionerror exception

class FiveDivisionError(Exception):
    "this is exception class called when five division error happens"
    pass


try:
     n1 = int(input("Enter first number"))
     n2 = int(input("Enter second number")) #5

     if n2 ==5:
         raise FiveDivisionError("Can not divide by five")
     div = n1/n2
     print(div)

except (FiveDivisionError, ZeroDivisionError) as var:
    print(var)

print("rest of code")
'''

#ex-2 Withdraw money from bank-
# - balance in bank should not be less  than 1000,  - user account will be blocked for an hours if user put 3 times wrong pin.
'''class BalanceExceptionError(Exception):
    pass
class AttempExceptionError(Exception):
    "this is exception class called when pin is incorrect"
    pass
attempts =1
def withdraw():
    global attempts
    saved_pin = 1234 # hard-coded
    balance =10000  # haed coded
    pin = int( input("Enter the PIN: "))
    if pin == saved_pin:
        try:
            amt = float(input("Enter amount to withdraw"))
            temp_bal = balance -amt
            if temp_bal <1000:
                raise BalanceExceptionError("Insufficent balance")
            balance = balance-amt
            print("Remained balance:", balance)
        except Exception as var:
            print(var)

    else:
        ans = input("Do you want to continue to again(y/n): ")
        if ans.lower() =='y':
            attempts +=1
            try:
                if attempts ==4:
                    raise  AttempExceptionError("Too many attempts, your account is blocekd for an hours")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you visit again")
            return

withdraw()

*/'''
#file handling
try:
    f = open("name.txt", mode='r')
    f.write("hello wordl")
except Exception as obj:
    print(obj)
else:
    f.close()


print("rest of code")














