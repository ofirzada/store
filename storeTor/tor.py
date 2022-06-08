from storeManagment import config


class Tor:
    def __init__(self, customers=[]):
        self.customers = customers

    def enqueue(self, customer):
        try:
            self.customers.append(customer)
            return True
        except:
            False

    def dequeue(self,count=1):
        while count>0 and len(self.customers)!=0:
            self.customers.pop(0)
            count=count-1

    def customersInTor(self):
        for cstrIndex in range(0,len(self.customers)):
            print(cstrIndex,vars(self.customers[cstrIndex]))