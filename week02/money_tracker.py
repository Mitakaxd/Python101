def list_user_data(all_user_data):
    for date, v in all_user_data.items():
        print(date)
        for transaction_type, transactions in v.items():
            for money, category in transactions:
                print(money,",",category,", ",transaction_type)


def show_user_incomes(all_user_data):
    return [(money,category)  for date,v in all_user_data.items() for money,category in v["New Income"]]


def show_user_savings(all_user_data):
    return [(money,category) for date,v in all_user_data.items() for money,category in v["New Income"]  if category == "Savings"]


def show_user_deposits(all_user_data):
    return [(money,category) for date,v in all_user_data.items() for money,category in v["New Income"] if category == "Deposit"]




def show_user_expenses(all_user_data):
    return [(money,category) for date,v in all_user_data.items() for money,category in v["New Expense"]]


def list_user_expenses_ordered_by_categories(all_user_data):
    print(sorted(show_user_expenses(all_user_data),key=lambda tuple_category : tuple_category[-1]))


def show_user_data_per_date(date, all_user_data):
    return all_user_data[date]


def list_income_categories(all_user_data):
    for date, v in all_user_data.items():
        for money,category in v["New Income"]:
            print(category)




def list_expense_categories(all_user_data):
    for date, v in all_user_data.items():
        for money,category in v["New Expense"]:
            print(category)


def add_income(income_category, money, date, all_user_data):
    all_user_data[date]["New Income"].append((money,income_category))
    return all_user_data

def add_expense(expense_category, money, date, all_user_data):
    all_user_data[date]["New Expense"].append((money,income_category))
    return all_user_data

def parse(filepath):
    data = {}
    current_data = ''
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            if '==' in line:
                current_data = ''.join(list(filter(lambda ch: ch!=' ' and ch!='=',line)))[:-1]
                data[current_data] = {}
                continue
            categories = line.split(', ')
            if categories[-1] not in data[current_data]:
                data[current_data][categories[-1][:-1]] = []
            data[current_data][categories[-1][:-1]].append((categories[0], categories[1]))
    return data

def execute(data,decision):
    if decision == 1:
        list_user_data(data)
    if decision == 2:
        date = input()
        print(show_user_data_per_date(date, data))
    if decision == 3:
        list_user_expenses_ordered_by_categories(data)
    if decision == 4:
        income_category, money, date = input().split()
        return add_income(income_category, money, date, data) 
    if decision == 5:
        expense_category, money, date = input()
        return add_expense(expense_category, money, date,data)
    return data



menu = ["1 - show all data ", "2 - show data for specific date", 
"3 - show expenses ordered by categories ", "4 - add new income", "5 - add new expense", "6 - exit"]

def main():
    
    data = parse("information.txt")
    print("Choose one of the following options to continue:")
    for option in menu:
        print(option)
    print(data)
    print("Your decision: ")
    decision = input()
    while int(decision) < 6:
        data = execute(data,int(decision))
        print("Choose one of the following options to continue:")
        for option in menu:
            print(option)
        decision = input()




if __name__ == '__main__':
    main()