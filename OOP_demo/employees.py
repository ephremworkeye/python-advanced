
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    # we use the init method here is define attributes here or to override the parent attributes
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll() # we inherited the calculate_payroll function therefore, in the future if changes in salaryEmployee calculate_payroll that automatically address the issue for the commission salary funciton
        return fixed + self.commission

class Manager(SalaryEmployee):
    # implicit inheritance
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours calling on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactors gadgets for {hours} hours.')

# multiple inheritace 
    # python supports multipe inheritance
    # allows class to derive mulitple other classes 

# case for multiple inheritance
    # we want a new class called TemporarySecratory that begaves like a Secretary in the productivity system, but is paid as an HourlyEmployee in the a payroll system

# Method Resolution Order(MRO)
    # A set of rules that diefines the search path  that python uses when searching for a method in cases of inheritance
    # Looks like an orderd list of classes
    # Each class has its own MRO
    # used by the super() function

class TemporarySecretary(HourlyEmployee, Secretary):
    pass