class Employee:
    # Class attribute
    company_name = "Tech Solutions Inc."

    def __init__(self, name, age, department, salary):
        # Instance attributes
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display_employee_details(self):
        """Instance method to display employee details."""
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    def update_salary(self, new_salary):
        """Instance method to update the salary of the employee."""
        self.salary = new_salary

    @classmethod
    def change_company_name(cls, new_company_name):
        """Class method to change the company name."""
        cls.company_name = new_company_name

    @staticmethod
    def is_retirement_age(age):
        """Static method to check if the given age is retirement age."""
        return age >= 65


# Creating objects of the Employee class
employee1 = Employee("Alice Johnson", 30, "Software Engineering", 80000)
employee2 = Employee("Bob Smith", 45, "Marketing", 60000)

# Displaying employee details
print("Employee 1 Details:")
employee1.display_employee_details()
print("\nEmployee 2 Details:")
employee2.display_employee_details()

# Updating salary of an employee
employee1.update_salary(85000)
print("\nUpdated Salary of Employee 1:")
employee1.display_employee_details()

# Changing the company name using class method
Employee.change_company_name("Innovative Tech Solutions")
print("\nUpdated Company Name for Employee 1 and Employee 2:")
print(f"Company Name: {Employee.company_name}")

# Checking retirement age using static method
print("\nRetirement Age Check:")
print(f"Is 30 retirement age? {Employee.is_retirement_age(30)}")
print(f"Is 65 retirement age? {Employee.is_retirement_age(65)}")