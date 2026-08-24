class Employee:

    employee_count = 0

    @classmethod
    def add(cls):
        Employee.employee_count += 1
 
emp1 = Employee()
emp2 = Employee()

emp1.add()
emp2.add()

print(emp1.employee_count)
