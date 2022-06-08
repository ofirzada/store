from .Person import Person
class customer(Person):
    def __init__(self, name, id, temp, hasMask,needIsolate,productList=[]):
        Person.__init__(self, name, id, temp, hasMask, needIsolate)
        self.productList = productList

    def add_products(self,product):
        self.productList.append(product)
