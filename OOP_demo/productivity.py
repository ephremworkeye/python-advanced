class ProductivitySystem:
    def track(self, employees, hours):
        print('=====================')
        for employee in employees:
            employee.work(hours)
        print('')