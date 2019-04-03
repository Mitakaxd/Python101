
class Income:
    def __init__(self,money,date,category):
        self.money=money
        self.date=date
        self.category=category
    def __str__(self):
        return "New Income: "+str(self.money) +" for "+str(self.category)+" at the "+str(self.date)
    def __repr__(self):
        return self.__str__()


class Expense:
    def __init__(self,money,date,category):
        self.money=money
        self.date=date
        self.category=category
    def __str__(self):
        return "New Expense: "+str(self.money) +" for "+str(self.category)+" at the "+str(self.date)
    def __repr__(self):
        return self.__str__()

