from .Registry import Regestry


class RegestryManagment:
    def __init__(self):
        self.registries = []
        self.regestry_managment()

    def regestry_managment(self):
        try:
            emp_choices = int(
                input(
                    'to check in items - prass 1 \nto add regestry prass 2 \n to check in employee to regestry prass 3 \n to see all transaction in regestries - prass 4 \n to see all if employe is should be issolated  - prass 5 \n to leave prass 0'))
            match emp_choices:
                case 1:

                    regs_id = input('enter regestry id ')
                    customer_name = input('enter customer name')
                    self.check_in_items(customer_name,regs_id)

                case 2:

                    id = input('enter regestry id ')
                    self.registries.append(Regestry(id))

                case 3:
                    regs_id = input('enter regestry id ')
                    emp_id = input('enter emp id ')
                    for reges in self.registries:
                        if reges.id == regs_id:
                            reges.shift_enter(emp_id)
                case 4:
                    for reges in self.registries:
                        print(reges.buyingHistory)

                case 5:
                    customer_name = input('enter customer name ')
                    unsafe_emp = []
                    for regs in self.registries:
                        for logs in regs.buyingHistory:
                            if logs.customer == customer_name:
                                unsafe_emp.append(logs.operator_id)
                    print('unsafe workers id')
                    print(unsafe_emp)
                case 0:
                    return
        except ValueError:
            print("invalid input please try again")
            self.regestry_managment()

        self.regestry_managment()

    def is_avalibale(self,regestry_id):
        for regs in self.registries:
            if regs.id==regestry_id:
                return regs.operator_id != None
        return False
    def check_in_items(self,customer_name,regs_id):
        products = []
        product_name=""
        while product_name != '0':
            product_name = input('enter productName name to end prass 0')

            products.append(product_name)
        for reges in self.registries:
            if reges.id == regs_id:
                reges.check_items(customer_name, products)
                return
        print('regestry not found')