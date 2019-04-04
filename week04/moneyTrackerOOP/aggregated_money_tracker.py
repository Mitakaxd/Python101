from parse_money_tracker import *
from category import *
def parsetoDate(line):
    line = ''.join(filter(lambda ch:ch != '=' and ch != ' ', list(line)))
    return line
def isDate(line):
    if "===" in line[0:5]:
        return True
    else:
        return False
def parsetoDict():
    lines = parse()
    result = {"income":[],"expense":[]}
    for line in lines:
        if isDate(line):
            curDate = parsetoDate(line)
            continue
        else:
            elems = line.split(', ')
            if "Expense" in elems[2]:
                obj = Expense(elems[0],curDate,elems[1])
                result["expense"].append(obj)
            else:
                obj = Income(elems[0],curDate,elems[1])
                result["income"].append(obj)
    return result


