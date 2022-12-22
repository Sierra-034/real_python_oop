class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('='*15)
        for employee in employees:
            employee.work(hours)

        print('')