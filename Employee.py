import datetime


class Employee:

    raise_amount = 1.04  # class variable
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first  # instance variables
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.no_of_emps += 1

    def apply_raise(self):
        return self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod   # using class method as an alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.no_of_emps)

emp1 = Employee('Vishwas', 'Sharma', 100000000)
emp2 = Employee('Anurag', 'Sharma', 2000000)

# print(emp2.__dict__)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

# pay = emp1.apply_raise()  # or Employee.raised_amount(emp1)
# print(pay)

emp_str_1 = 'John-Doe-700000'
emp_str_2 = 'Steve-Smith-450200'
emp_str_3 = 'Jane-Doe-900000'

new_emp1 = Employee.from_string(emp_str_1)
print(Employee.no_of_emps)

print(new_emp1.email)

my_date = datetime.date(2021, 7, 23)
print(Employee.is_workday(my_date))
