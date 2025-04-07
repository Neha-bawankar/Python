# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class (Single Inheritance)
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}")

if __name__ == "__main__":
    # Creating an Employee object
    employee = Employee("John Doe", 30, "E123")
    employee.display_employee_info()