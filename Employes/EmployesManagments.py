import random

from .Employe import Employee


class EmployeManagment:
    def __init__(self):
        self.employes = []
        self.employe_managment()

    def employe_managment(self):
        try:
            emp_choices = int(
                input(
                    ' to add employees prass 1 \n to check in emp prass 2\n to check out emp prass 3  \n to see all employees history prass 4 \n to leave prass 0 \n'))
            match emp_choices:
                case 1:
                    name = input('enter employee name ')
                    id = input('enter employee id ')
                    e1 = Employee(name, id, random.randint(27, 45), random.randint(0, 8) == 0,
                                  random.randint(0, 7) != 0)
                    self.employes.append(e1)
                case 2:
                    name = input('enter employee name ')
                    self.check_in(name)
                case 3:
                    name = input('enter employee name ')
                    self.check_out(name)
                case 4:
                    print(self.employes)
                    self.see_all_emp()
                case 0:
                    return
        except ValueError:
            print("invalid input please try again")
            self.manageTor()

        self.employe_managment()

    def see_all_emp(self):
        for emp in self.employes:
            print(vars(emp))

    def check_in(self, employee_name):
        for emp in self.employes:
            if emp.name == employee_name:
                emp.check_in()
                return True
        print("emp not found")
        return False

    def check_out(self, employee_name):
        for emp in self.employes:
            if emp.name == employee_name:
                emp.check_out()
                return True
        print("emp not found")
        return False
