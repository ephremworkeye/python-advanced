class ProductivitySystem:
    def track(self, employees, hours):
        print('=====================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')


class ManagerRole:
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class SecretaryRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesRole:
    def work(self, hours):
        print(f'{self.name} expends {hours} hours calling on the phone.')

class FactoryRole:
    def work(self, hours):
        print(f'{self.name} manufactors gadgets for {hours} hours.')
