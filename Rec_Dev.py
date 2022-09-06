from Employee import Employee


class Recruiter(Employee):
    # Create a class for employee's named Recruiter.

    def __init__(self, name, salary, days):
        super().__init__(name, salary, days)

    def work(self):
        # Method that initialization what Recruiter doing at work.
        return f"I come to the office and start to hiring."

    def __str__(self):
        # Method that show us profession and name of the worker.
        return f"{self.__class__.__name__} : {self.name}"

    def check_salary(self):
        # Calculates the salary for the number of days.
        return f"Your salary is {self.salary * self.days} for {self.days} days"


class Developer(Employee):
    # Create a class for employee's named Developer.

    def __init__(self, name, salary, days=0, tech_stack=[]):
        super().__init__(name, salary, days)
        self.tech_stack = tech_stack

    def work(self):
        # Method that initialization what Developer doing at work.
        return f"I come to the office and start to coding."

    def __str__(self):
        # Method that show us profession and name of the worker.
        return f"{self.__class__.__name__} : {self.name}"

    def check_salary(self):
        # Calculates the salary for the number of days.
        return f"Your salary is {self.salary * self.days} for {self.days} days"

    def check(self, other):
        # Technology comparison from 2 Developers.
        return len(self.tech_stack) - len(other.tech_stack)

    def obj(self, other):
        # Comparison new object from 2 Developers, their technologies and show better salary from them.
        name = f"{self.name} {other.name} {set(self.tech_stack + other.tech_stack)} {max(self.salary, other.salary)}"
        return name
