from typing import List
from employee import CommissionEmployee, Employee, HourlyEmployee, SalaryEmployee


class Company:
    def __init__(self) -> None:
        self.employees: List[Employee] = []
    
    def add_employees(self, new_employee: Employee):
        self.employees.append(new_employee)
    
    def display(self):
        print(f"Company has {len(self.employees)} employees. Details below")
        for index, employee in enumerate(self.employees):
            print(f"{index + 1}. {employee.fname} {employee.lname} drawing salary of ${employee.calculate_paycheck():,.2f}")

def main():
    company = Company()
    company.add_employees(SalaryEmployee('John', 'Doe', 50000))
    company.add_employees(HourlyEmployee('Jane', 'Doe', 40, 15))
    company.add_employees(CommissionEmployee('Bob', 'Brown', 40000, 5, 20))
    company.display()
main()
