from employees import Employee, SalaryEmployee, CommissionEmployee, HourlyEmployee, \
    Manager, Secretary, SalesPerson, FactoryWorker, TemporarySecretary
from hr import PayrollSystem
from productivity import ProductivitySystem

# salary_employee = SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
# commision_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
print(TemporarySecretary.__mro__)

manager = Manager(1, 'John Smith', 1500)
secretory = Secretary(2, 'Jane Doe', 1200)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(4, 'Pete Peterson', 40, 15)
temporary_secretory = TemporarySecretary(5, 'Robin Williams', 40, 9)


employees = [
    manager,
    secretory,
    sales_guy,
    factory_worker,
    temporary_secretory
]

productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
