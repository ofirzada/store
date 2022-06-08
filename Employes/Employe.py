
from datetime import datetime



from storeManagment.Person import Person

class Employee(Person):
    def __init__(self, name, id, temp, hasMask, needIsolate):
        Person.__init__(self, name, id, temp, hasMask, needIsolate)
        self.shifts = []
        self.is_working=False
    def check_in(self):
        if self.is_working:
            print("employe {name} is already working".format(name = self.name))
        else:
            if self.isSafe:
                checkInTime = datetime.now()
                print(checkInTime)
                work_time={'checkIn': checkInTime,'checkOut':""}
                self.shifts.append(work_time)
                self.is_working = True
            else:
                print("employe {name} is not safe! fine 4o sheckels ".format(name=self.name))

    def check_out(self):
        if self.is_working:
            self.shifts[-1]['checkOut']=datetime.now()
            self.is_working=False
        else:
            print("employe {name} is not working".format(name=self.name))
