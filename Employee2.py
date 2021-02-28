class Employee:

    raise_amount = 1.04  # class variable
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # instance variables
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.no_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        return self.pay * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Nick', 'Wayne', 700000, 'Python')
dev_2 = Developer('Bruce', 'Wayne', 800000, 'Java')

# print(dev_1.email)
# print(dev_2.pay)

mgr_1 = Manager('Sue', 'Riley', 5670321, [dev_1])
# mgr_1.print_emp()
#
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()


# print(isinstance(mgr_1, Manager))
# print(issubclass(Developer, Employee))