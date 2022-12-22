import hr
import employees
import productivity

if __name__ == '__main__':
    salary_employee = employees.Manager(1, 'John Smith', 1500)
    hourly_employee = employees.Secretary(2, 'Jane Doe', 1200)
    commission_employee = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = employees.FactoryWorker(4, 'Pete Peterson', 40, 15)

    employees = [
        salary_employee,
        hourly_employee,
        commission_employee,
        factory_worker,
    ]

    productivity_system = productivity.ProductivitySystem()
    productivity_system.track(employees, 40)

    payroll_system = hr.PayrollSystem()
    payroll_system.calculate_payroll(employees)
