class Employee:
    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
    
    def weekly_pay(self):
        return self.salary / 52
