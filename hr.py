class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('='*15)
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}', end='\n')
            if employee.address:
                print('- Sent to:')
                print(employee.address, end='\n\n')

class SalaryPolicy:
    def __init__(self, weekly_salary) -> None:
        self.weekly_salary = weekly_salary

    def calculate_payroll(self) -> str:
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate) -> None:
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionsPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commissions) -> None:
        super().__init__(weekly_salary)
        self.commissions = commissions

    def calculate_payroll(self) -> str:
        fixed = super().calculate_payroll()
        return fixed + self.commissions
