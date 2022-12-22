class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('='*15)
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')

        print('')

class ManagerRole:
    def work(self, hours):
        return f'Screams and yells for {hours} hours.'

class SecretaryRole:
    def work(self, hours):
        return f'Expends {hours} hours doing office paperwork.'

class SalesRole:
    def work(self, hours):
        return f'Expends {hours} hours on the phones.'

class FactoryRole:
    def work(self, hours):
        return f'Manufactures gadgets for {hours} hours.'
