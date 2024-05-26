class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def calculate_paycheck():
        pass

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary / 52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, num_hours, hourly_rate):
        super().__init__(fname, lname)
        self.num_hours = num_hours
        self.hourly_rate = hourly_rate
    
    def calculate_paycheck(self):
        return self.num_hours * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, num_sales, com_rate):
        super().__init__(fname, lname, salary)
        self.num_sales = num_sales
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        return super().calculate_paycheck() * self.num_sales * self.com_rate
    

    
