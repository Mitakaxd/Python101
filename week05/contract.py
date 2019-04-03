class Contract:
    def __init__(self,car,person,money):
        self.car=car
        self.person=person
        self._money=money
    def get_money(self):
        return self._money*1.95
    def set_money(self,value):
        self._money=value

contract_mazda=Contract('mazda','Slavqna',7500)
print(contract_mazda.get_money())