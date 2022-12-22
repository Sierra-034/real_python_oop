class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('='*15)
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}', end='\n')

class Employee:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate) -> None:
        super().__init__(id, name)
        self.hous_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hous_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission) -> None:
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
