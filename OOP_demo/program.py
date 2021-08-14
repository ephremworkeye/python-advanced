import hr
import employees
import productivity
import contacts

# salary_employee = SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
# commision_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# print(TemporarySecretary.__mro__)

manager = employees.Manager(1, 'John Smith', 1500)
manager.address = contacts.Address(
    '123 Admin Road',
    'concord',
    'WA',
    '98008'
)
secretory = employees.Secretary(2, 'Jane Doe', 1200)
secretory.address = contacts.Address(
    '123 Admin Road',
    'Seattle',
    'TX',
    '98008'
)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Pete Peterson', 40, 15)
temporary_secretory = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)


employees = [
    manager,
    secretory,
    sales_guy,
    factory_worker,
    temporary_secretory
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
