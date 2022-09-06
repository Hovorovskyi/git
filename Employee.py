from Exception import EmailAlreadyExistsException

class Employee():
    # Create a primitive class for initialization and further work with it.

    def __init__(self, name: str, salary: int, email: str, days=0):
        self.name = name
        self.salary = salary
        self.days = days
        self.email = email
        self.validate()
        self.save_email()

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

    def save_email(self):
        with open("emails.txt", "a+") as filename:
            filename.write(self.email.lower() + "\n")

    def validate(self):
        with open("emails.txt", "r") as filename:
            if self.email.lower() in filename.read():
                raise EmailAlreadyExistsException("Email is already taken!")
