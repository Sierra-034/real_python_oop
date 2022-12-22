class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating payroll')
        print('='*15)
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}', end='\n')

