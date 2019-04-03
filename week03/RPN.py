import unittest
def calculate(expression):
    lst=expression.split(' ')
    endlist=[]
    for elem in lst:
        if elem!='+' and elem!='-' and elem!='*' and elem!='/':
            endlist.append(elem)
        else:
            firstnum=endlist[-1]
            endlist.pop()
            if elem =='+':
                secondnum=endlist[-1]
                endlist.pop()
                endlist.append(int(firstnum) + int(secondnum))
            elif elem=='-':
                secondnum=endlist[-1]
                endlist.pop()
                endlist.append(int(secondnum) - int(firstnum))
            elif elem=='*':
                secondnum=endlist[-1]
                endlist.pop()
                endlist.append(int(firstnum) * int(secondnum))
            elif elem=='/':
                secondnum=endlist[-1]
                endlist.pop()
                endlist.append(int(secondnum) / int(firstnum))
            else:
                endlist.append(int(eval(tolower(elem)+"("+firstnum+')')))
    return int(endlist[-1])

class TestRPN(unittest.TestCase):
    def test_1(self):
        self.assertEquals(calculate("4 7 3 + *"),40)
    def test_2(self):
        self.assertEquals(calculate("100 3 * 20 -"), 280)
    def test_3(self):
        self.assertEquals(calculate("100"),100)
if __name__=="__main__":
    unittest.main()