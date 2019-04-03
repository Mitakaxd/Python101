from cashdesk import Bill
from itertools import groupby
class Bill:
    def __init__(self,ammount):
        if type(ammount)!=type(5):
            raise TypeError()
        if ammount<0:
            raise ValueError()
        self.ammount=ammount
    def __str__(self):
        return "Bill ammount: "+str(self.ammount)
    def __repr__(self):
        return str(self.ammount)
    def __int__(self):
        return self.ammount
    def __eq__(self, other):
        return self.ammount==other.ammount
    def __hash__(self):
        return hash(str(self))

class BillBatch:
    def __init__(self, lstBills):
        self.lstBills=lstBills
    def __len__(self):
        return len(self.lstBills)
    def __int__(self):
        return self.total()
    def total(self):
        return sum(map(lambda bill: int(bill),self.lstBills))
    def __str__(self):
        output=[]
        for bill in self.lstBills:
            output.append(str(bill))
        return str(output)
    def __repr__(self):
        return self.__str__()
    def __getitem__(self, index):
        return self.lstBills[index]

class CashDesk:
    def __init__(self):
        self.listBills=[]
    def take_money(self,money):
        self.listBills.append(money)
    def total(self):
        result=0
        for money in self.listBills:
            result+=int(money)
        return result
    def inspect(self):
        dictofMoney={}
        for money in self.listBills:
            if type(money) is BillBatch:
                for bill in money:
                    if str(bill) in dictofMoney:
                        dictofMoney[str(bill)]+=1
                    else:
                        dictofMoney[str(bill)]=1
            else:
                if str(money) in dictofMoney:
                    dictofMoney[str(money)]+=1
                else:
                    dictofMoney[str(money)]=1
        for key,value in dictofMoney.items():
            print(key, " ",value)
        #self.listBills.sort(key=lambda elem:int(elem))