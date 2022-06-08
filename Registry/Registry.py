from datetime import datetime


class Regestry:
    def __init__(self, id, operator_id=None):
        self.operator_id = operator_id
        self.id = id
        self.buyingHistory = []
        self.operatorsHistory = []
        if operator_id != None:
            self.operatorsHistory.append({'opperator': operator_id, 'checkinTime': datetime.now()})

    def check_items(self, customer_name, productList):
        self.buyingHistory.append({'customer': customer_name, 'items': productList, 'buyingTime': datetime.now(),
                                   'operator_id': self.operator_id})

    def shift_enter(self, operator_id):
        self.operator_id = operator_id
        self.operatorsHistory.append({'opperator': self.operator_id, 'checkinTime': datetime.now()})

    # def show_products_history(self):
    #     return
    # def show_emp_history(self):
    #     for logs in self.operatorsHistory:
    #         print(vars(logs.opperator),logs.checkinTime)
