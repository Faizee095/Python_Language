class Employee():
    increment_percent=1.1
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def employee_details(self):
        print('{} {} {}'.format(self.name,self.age,self.salary))

    def increment(self):
        self.salary=int(self.salary * Employee.increment_percent)

employee1=Employee('John',25,15000)
employee2=Employee('Samuel',35,90000)


# print(Employee.increment(employee2))
employee1.increment()
print(employee1.salary)
