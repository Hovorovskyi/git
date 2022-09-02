class Employee():

    def __init__(self, name: str, salary: int, days=0):
        self.name = name
        self.salary = salary
        self.days = days

    def work(self):
        return f'I come to the office.'

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary



class Recruiter(Employee):

    def __init__(self, name, salary, days):
        super().__init__(name, salary, days)

    def work(self):
        return f"I come to the office and start to hiring."

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"

    def check_salary(self):
        return f"Your salary is {self.salary * self.days} for {self.days} days"


class Developer(Employee):

    def __init__(self, name, salary, days=0, tech_stack=[]):
        super().__init__(name, salary, days)
        self.tech_stack = tech_stack

    def work(self):
        return f"I come to the office and start to coding."

    def __str__(self):
        return f"{self.__class__.__name__} : {self.name}"

    def check_salary(self):
        return f"Your salary is {self.salary * self.days} for {self.days} days"

    def check(self, other):
        return len(self.tech_stack) - len(other.tech_stack)

    def obj(self, other):
        name = f"{self.name} {other.name} {set(self.tech_stack + other.tech_stack)} {max(self.salary, other.salary)}"
        return name


if __name__ == '__main__':
    rec = Recruiter("Jo", 75, 5)
    Max_dev = Developer("Max", 120, 5, ["python", "C++", "PHP", "JS"])
    Fill_dev = Developer("Fill", 100, 10, ["python", "java"])


    print(rec.work())
    print(Max_dev.work())
    print(Max_dev.__str__())
    print(rec.__str__())
    print(Fill_dev.check_salary())
    print(rec > Max_dev)
    print(Max_dev.check(Fill_dev))
    print(Max_dev.obj(Fill_dev))