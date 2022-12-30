class ProductivitySystem:
    def __init__(self) -> None:
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('Invalid role_id')

        return role_type()
    
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('='*15)
        for employee in employees:
            employee.work(hours)

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
