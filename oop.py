class Employee:
    raise_amount = 0.1

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def apply_raise(self):
        total_payable = int(self.salary + self.salary * self.raise_amount)
        return "After salary increase:", total_payable

    def __str__(self):
        return f"Every employee has name: {self.name} and {self.emp_id} and salary {self.salary}"

    @classmethod
    def raise_salary(cls, amnt):
        cls.raise_amount = amnt
        # return f"Updated salary for employee {cls.raise_amount}"

    @classmethod
    def form_string(cls, string):
        name, emp_id, salary = string.split("-")
        return cls(name, emp_id, salary)

    @staticmethod
    def is_workday(day):
        return True if day.weekday() == 5 or day.weekday() == 6 else False


class Developer(Employee):
    pass
    # def __init__(self, member, salary):
    #     self.member = member
    #     self.salary = salary


import datetime

my_date = datetime.date(2022, 6, 26)

dev_1 = Developer("SSF", 2022, 100000)
dev_2 = Developer("BKD", 2233, 50000)
print(dev_1)
print(dev_2)

# print(help(Developer))

dev_1.raise_salary(0.5)
print(dev_1.apply_raise())

# emp_1 = Employee("Biplab", 2022, 10000)
# emp_2 = Employee("Aman", 2233, 150000)
# emp_str_1 = "Mubin-3284-980000"
# emp_str_2 = "Rony-87234-80000"
#
# new_emp = Employee.form_string(emp_str_1)
# new_emp2 = Employee.form_string(emp_str_2)
# print(new_emp)
# print(new_emp2)
#
# print(Employee.is_workday(my_date))

# # print(emp_1.emp_id)
# # print(emp_1.name)
# print(emp_1.__dict__)
# # print(emp_2.emp_id)
# # print(emp_2.name)
# print(emp_2.__dict__)
# Employee.raise_salary(0.5)
# print(emp_1.apply_raise())
# print(emp_2.apply_raise())
