from storeManagment import config
from storeManagment.Customer import customer
from .tor import Tor



"""random.randint(27, 45)"""
"""

# random.randint(0, 1) == 1
def insert(storeTor):
    name = input('enter customer name ')
    id = input('enter customer id ')
    c1 = customer(name, id, True, True)
    if storeTor.enqueue(c1):
        print(name + " has enter tor! \n")
    else:
        print(name + " is not healthy \n")
        print(vars(c1))
    return storeTor


def manageTor(storeTor):
    try:
        choices = int(input(config.oppeningMessage))
        match choices:
            case 1:
                storeTor = insert(storeTor)
            case 2:
                customersToEnter = int(input('how many customers to enter the store?'))
                storeTor.dequeue(customersToEnter)
                print(str(customersToEnter) + " customers where removed")

            case 3:
                (storeTor.customersInTor())
                print()

            case 0:
                return
    except ValueError:
        print("invalid input please try again")

        manageTor(storeTor)

    manageTor(storeTor)


storeTor = Tor()
print("welcom to the store!")
manageTor(storeTor)
print('thanks for comming')
"""

class torManagment:
    def __init__(self):
        self.storeTor = Tor()
        self.manageTor()

    def insert(self):
        name = input('enter customer name ')
        id = input('enter customer id ')
        c1 = customer(name, id, 11, True,False)
        print(c1.isSafe())
        if c1.isSafe():
            self.storeTor.enqueue(c1)
            print(name + " has enter tor! \n")
        else:
            print(name + " is not healthy \n")
            print(vars(c1))

    def manageTor(self):
        try:
            choices = int(input(config.torMessage))
            match choices:
                case 1:
                    storeTor = self.insert()
                case 2:
                    customersToEnter = int(input('how many customers to enter the store?'))
                    self.storeTor.dequeue(customersToEnter)
                    print(str(customersToEnter) + " customers where removed")

                case 3:
                    (self.storeTor.customersInTor())
                    print()

                case 0:
                    return
        except ValueError:
            print("invalid input please try again")
            self.manageTor()
        self.manageTor()

