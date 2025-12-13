#ex -1 creating class and object
class Employee:
    def __init__(self, nm, ag):
       self.name = nm
       self.age = ag
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')


e1 = Employee('raj', 22)
e2 = Employee('rohit', 45)

e1.display()
e2.display()

# ex-2 creating class
'''class Student:
    def __init__(self):
        self.fees = 2000
        self.age =15


s1 = Student();
s2 =Student();

print(s1.__dict__)


#default constructor
class dog:
    pass

d1 = dog()

'''


'''class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title of Book: ", self.title)
        print("Auhtor of Book: ", self.author)
        print("Price of book: ", self.price)

b1 = Book("Maths", "Alice", 323)
b1.display()


class BankAccount:
    def __init__(self, owner, balance =0):
        self.owner = owner
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print("Deposit: ", amount)

    def withdraw(self, amount):
         if amount > self.balance:
             print("Sufficient balance")
         else:
           self.balance -= amount
           print("Withdraw:", amount)

    def  check_balance(self):
        print("Remaining balance: ", self.balance)

    def display(self):
        print(f"Owner Name: {self.owner} Balance in account: {self.balance}")


acc1 = BankAccount("jenny", 15000)
acc1.display()
acc1.deposit(5000)
acc1.display()
acc1.check_balance()
acc1.withdraw(2000)
acc1.check_balance()

#step for object creation
#1. memory allocation for object
#2. memory reference retuned to the object.
#3. memory refrence automattically passes inside constructor.
#4. Constructor create/initialize varible at the memory refrence

#ex-1How to access calss member/ accessing attribute outside the class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name is {self.name} and age is {self.age}")



e1 = Employee("harry", 28)
e2 = Employee("Jessy", 23)


# outside the class
print(e1.age)


#Buit-in class attribute-
print(e1.__dict__)
print(e1.__doc__)
print(e1.__class__)
print(e1.__dir__())
print(e1.__module__)
#built-in class function-

class employee:
    def __init__(self, salary, name):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

em1 = employee(2232, 'ram')
em2 = employee(2322, 'shyam')

print(getattr(em1, "name"))
setattr(em1, "name", "rohit")
print(em1.name)
#print(delattr("name"))
print(hasattr(em1, "salary"))


#instance variable
class student:
    def __init__(self, roll_no, section):
       self.roll_no = roll_no
       self.section = section


    def display(self):
        print(f"student roll no is {self.roll_no} and their section is {self.section}")

stu1 = student(12, "A")
stu2 = student (13, 'B')

stu1.display()
#stu2.display()

stu2.roll_no = 14
stu2.display()

del stu2
#stu2.display()

stu1.display()
'''
'''''
#class variable  - variable made for entire class(all object) , only one cpy is created and distributed to all object.
class Employee:
# class varibal creaetd
    company_name = "wipro"
    def __init__(self, mn, sal):
        self.name = mn
        self.salary = sal


e1 = Employee("jay", 30000)
e2 = Employee("vijay", 50000)

print(Employee.company_name)
print(e1.company_name)

#modify
Employee.company_name = "TCS"
print(Employee.company_name)


#class method - method which works on class variable , first argument is class refrence
#Made using decorator '@classmethod'

class employee:
    company_name = "infosys"
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal

        #class method
    @classmethod
    def get_company_name(cls):
        print(f"company name is : " , cls.company_name)


e3 = employee("raj", 83467)
e4 = employee("swraj", 275456)

employee.get_company_name()

#setter and getter
#setter method - set values of instance varibale
#getter method - get value of instance varibale

class Employee:
    def setName(self, nm):
        self.name = nm

    def getName(self):
        print("The name is: ", self.name)

e1 = Employee()
e2 = Employee()

e1.setName(input('Enter the name: '))
e2.setName(input("enter the name: "))
print("e1 object is : ", e1.__dict__)
print("e2 object is:", e2.__dict__)

e2.getName()
e1.getName()


#inheritence - deriving a new class from an existing class so that new class inherital member(attribute + method) of existing class is called as inheritence
#object class - All classes in python are derived from built in object class
class  company:
    bonus = 2000
    def display(self):
        print("This is employee class method")

class Manager(company):
    bonus1 = 5000
    def show(self):
        print("This is manager class method")

e1 = company()
m1 = Manager()


e1.display()
m1.show()
print(m1.bonus)

#constructor in inheritence
# by default constructor of parent class available to child class

class Father:
    def __init__(self):
        print("Father construcor called")
        self.vehicle = "scooter"


class child(Father):
    def __init__(self):
        print("Son construtor called")
        self.vehicle = "BMW"


s = child()
print(s.__dict__)

#super function - using super() fucntion, we can access parent class properties.
# this function return a temporary object which contain refrence to parent class


class Computer(object):
    def __init__(self):
        self.RAM = '8gb'
        self.storage = '512gb'
        print("Computer class constructor called")

class Mobile(Computer):
    def __init__(self):
        print("Son construtor called")
        self.vehicle = "BMW"

Apple = Mobile()
print(Apple.__dict__)

#Type of inheritence
#1- single inheritence
#2 - Multilevel inheritence
class Human_being(object):
    def __init__(self):
        print("Human being constructor called")
        self.name = input("enter your name")

class Employee(Human_being):

    def __init__(self):
        #super().__init__()
        print("Employee class  constructor called")
        self.salary = float(input("enter your salary: "))


class Manager(Employee):
    def __init__(self):
        #super().__init__()
        print("Manager constructor called")
        self.bonus = input("enter your bonus")



m1 = Manager()
e1 =Employee()
h1 = Human_being()
'''
# hierarchy inheritence - child can not access each other property

class Person:
    def __init__(self,nm,ag):
        self.name =nm
        self.age = ag
    def display(self):
        print("This is person display method")


class Employee(Person):
    def __init__(self, sal):
        self.salary = sal
    def display2(self):
        print("This is employee display method")

class Student(Person):
    def __init__(self,nm, ag,m):
        super().__init__(nm,ag)
        self.marks= m

    def display3(self):
            print("This is Student display method")


s1 = Student('jay',21,90)
e1 = Employee(40000)

s1.display()
print(s1.__dict__)

#p1.display2() # attribute error


#multiple inheritence - class is derived from multiple base class

class country:
    office ='Delhi'

class State:
    office ="Mumbai"

class District(country, State):
    pass

d= District()
print(d.office)


#with constructor
class country:
    def __init__(self):
        print("country class constructor")
        self.office ='Delhi'

class State:
    def __init__(self):
     super().__init__()
     print("state  class constructor")
     self.office ="Mumbai"

class District(country, State):
    pass

d= District()

#print(d.office)
print(d.__dict__)


#Encapsulation -  wrapping up data and method working on data together in a single unit(class) is called as encapsulation

class Employee:
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary

    def display(self):
        print(f"name is : {self.name} and salary is : {self.salary}")

# encapsulation we can not write this
#object_name.name

#ex-2
class Finance:
    def __init__(self):
        self.revenue = 10000
        self.number_of_sales = 112

f1 = Finance()

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.revenue =1
        print(f1.revenue)

h1 = HR()
print(f1.__dict__)

#Access Modifier in python - we restrict data access outside the class in encapsulation
# three access specifier -\public, private , protected
#public member - Accessible anywhere by using object reference
#private member - Accessible within the class, accessible  via method only


class Finance:
    def __init__(self):
        self.__revenue = 10000 # private data
        self._number_of_sales = 112 # protected data

f1 = Finance()
#print(revenue)
print(f1.__dict__)
class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.revenue =1
        #print(f1.revenue)

h1 = HR()
print(f1.__dict__)


# ex-2
class Finance:
    class_variable = "hhh"
    def __init__(self):
        self.__revenue = 100000 ##private data
        self.__number_of_sales = 114  #private data

    @classmethod
    def display(self):
        print(f"revenue is :{self.__revenue}  and number of sales {self.__number_of_sales}")
        self.revenue = 2000000
        print(f"revenue is :{self.revenue}  and number of sales {self.__number_of_sales}")


f1 = Finance()
f1.display()


#polymorphism - in python is an ability of pyhton object to take many forms
#ex-1
# + :- pyhton object - diffrent behaviour in different situation
print(10+20)
print("Hello" + "world")

#ex  polymorphism with inheritence

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print("name is:", self.name)
        print("color is: ", self.color)
        print("price is: ", self.price)


    def max_speed(self):
        print("maximum speed limit is 100")

    def gear(self):
        print("gear change is 6")

class car(Vehicle):
    def max_speed(self):
        print("maximum speed limit is 140")

    def gear(self):
        print("gear change is 7")


v1 = Vehicle("Truck", "red", 1000000)
c1 = car("mg", "white", 18373600)
v1.get_details()
c1.get_details()
v1.max_speed()
c1.max_speed()


#polymorphism with function and class


class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_spedd(self):
        print("max speed is 200")

class Ferreri:
    def fuel_type(self):
        print("Petrol")

    def max_spedd(self):
        print("max speed is 180")

def car_details(obj):
    obj.fuel_type()
    obj.max_spedd()
bmw = BMW()
Ferreri = Ferreri()


car_details(bmw)
print("-----")
car_details(Ferreri)

#overloading -  when same operator behave depending on values
num1 = 10
num2 =20
print(num1+num2)





#Abstraction - the process by which data and function are defined in such a way that only essential details can be seen and unnecessary implementaions are hidden called data Abstraction
#by using abc module you can achieved abtraction in python -
#abstract method - method that has a declaration but not have implementation
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("White")   # we can not create object of abstract class

class Maruti(Car):
    def mileage(self):
        print("mileage is 30kmph")

class TATA(Car):
    def mileage(self):
        print("mileage is 35kmph")


class MG(Car):
    def mileage(self):
        print("mileage is 45kmph")



#c1 =Car()
m1 = Maruti()
t1 = TATA()
d1 = MG()

t1.mileage()
m1.mileage()
d1.mileage()
t1.color()
m1.color()
d1.color()


#Abstract class - a class which contain one or more abstract method and concrete method
# Abstract class must have at least one abstract method



#callable() in python - it is bulit in function it return true or false
#object which can be called whenever required.
# object having _call_()method in their class


x = 100
print(callable(x))


def add(a,b):

    return a+b


a1 =add(10,20)
print(a1)
print(callable(add))

