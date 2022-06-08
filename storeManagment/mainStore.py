import config
from Employes.EmployesManagments import EmployeManagment
from Registry.RegestryManagment import RegestryManagment
from storeTor.torManager import torManagment


class storeManger:
    def __init__(self):

        self.manageStore()

    def manageStore(self):
        try:
            choices = int(input(config.storeMessage))
            match choices:
                # torManager
                case 1:
                    self.storeTor = torManagment()

                case 2:
                    self.employess = EmployeManagment()
                case 3:

                    self.RegestryManagments = RegestryManagment()

                case 0:
                    return
        except ValueError:
            print("invalid input please try again")
            self.manageStore()
        self.manageStore()


storeManger()
