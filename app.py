import traceback

from Rec_Dev import Recruiter
from Rec_Dev import Developer
from Employee import Employee
from Exception import EmailAlreadyExistsException
from datetime import datetime


def main():
    #rec = Recruiter("Jo", 75, 5)
    #Max_dev = Developer("Max", 120, 5, ["python", "C++", "PHP", "JS"])
    #Fill_dev = Developer("Fill", 100, 10, ["python", "java"])
    Employee("Fill", 21, "hfsgkh@gmail.com")

    # print(rec.work())
    # print(Max_dev.work())
    # print(Max_dev.__str__())
    # print(rec.__str__())
    # print(Fill_dev.check_salary())
    # print(rec > Max_dev)
    # print(Max_dev.check(Fill_dev))
    # print(Max_dev.obj(Fill_dev))

if __name__ == "__main__":
    try:
        main()
    except EmailAlreadyExistsException:
        log_date = f"{datetime.now()} | {traceback.format_exc()}"
        with open("logs.txt", "a+") as fl:
            fl.write(log_date)
