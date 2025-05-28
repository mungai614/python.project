class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def details(self):
        print( self.name,"is the",self.position,)

employee1 = Employee("John", "CEO", 20000)
print(employee1.name, employee1.position, employee1.salary)

employee2 = Employee("Jane", "MD", 140000)
print(employee2.name, employee2.position, employee2.salary)
employee3 = Employee("Eunice", "SCT", 20000)
print(employee3.name, employee3.position, employee3.salary)
employee4 = Employee("Mark", "MN", 20000)
print(employee4.name, employee4.position, employee4.salary)