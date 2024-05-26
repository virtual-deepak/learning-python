from typing import List
from employee import Employee


class Company:
    def __init__(self) -> None:
        self.employees: List[Employee] = []
    
    def add_employees(self, new_employee: Employee):
        self.employees.append(new_employee)
    
    def display(self):
        print(f"Company has {len(self.employees)} employees. Details below")
        for index, employee in enumerate(self.employees):
            print(f"{index + 1}. {employee.fname} {employee.lname} drawing weekly salary of ${employee.weekly_pay():,.2f}")

def main():
    company = Company()
    company.add_employees(Employee('John', 'Doe', 50000))
    company.add_employees(Employee('Jane', 'Doe', 55000))
    company.add_employees(Employee('Bob', 'Brown', 65000))
    company.display()
main()
