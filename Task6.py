class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("---")

emp1 = Employee("Dheenu", 25, 30000)
emp2 = Employee("Meenu", 28, 45000)

emp1.display_details()
emp2.display_details()