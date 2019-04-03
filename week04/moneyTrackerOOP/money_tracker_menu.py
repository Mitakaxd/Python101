from aggregated_money_tracker import *
from category import *
class MoneyTrackerMenu:
    menu={
    1:" Show all user data(incomes and expenses).",
        2: " Show user data for specific date.",
    3: " Lists all expense categories.",
    4: " Lists all income categories.",
    5: " The user can add new income or expense for specific date and category.",
    6: " The user must be able to create new categories."
}
    def pickoption(self,option):
        if option==0:
            return "Goodbye!"
        else:
            if option==1:
                for k in self.aggregate["income"]:
                    print(k)
                for k in self.aggregate["expense"]:
                    print(k)
            elif option==3:
                print(self.aggregate["expense"])
            elif option==4:
                print(self.aggregate["income"])
            elif option==2:
                print("Give me a date: ")
                date=input()
                for item in self.aggregate["income"]:
                    if item.getDate()==date:
                        print(item)
                for item in self.aggregate["expense"]:
                    if item.getDate()==date:
                        print(item)
            elif option==5:
                print("give me income or expense, money, date and category")
                typeof=input()
                money=input()
                date=input()
                category=input()
                if typeof =="income":
                    self.aggregate["income"].append(Income(money,date,category))
                else:
                    self.aggregate["expense"].append(Expense(money,date,category))
        for k,v in self.menu.items():
            print(k,". ",v)
        option=int(input())
        self.pickoption(option)
    def __init__(self):
        self.aggregate=parsetoDict()
        for k,v in self.menu.items():
            print(k,". ",v)
        option=int(input())
        self.pickoption(option)

def main():
    menu=MoneyTrackerMenu()
if __name__ == '__main__':
    main()