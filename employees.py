from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook

class EmployeeDatabase:
    def __init__(self) -> None:
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager',
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary',
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales',
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory',
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary',
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_address = AddressBook()

    def employees(self):
        return [self._create_employee(**employee) for employee in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_address.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
