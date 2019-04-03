import unittest


def simplify_fraction(fraction):
    x,y = fraction
    def findNod(fraction):
        x,y = fraction
        if x == 0 or y == 0:
            return 0
        if x == y:
            return x
        elif x > y:
            return findNod((x-y,y))
        else:
            return findNod((x,y-x))
    nod = findNod(fraction)
    if nod == 0:
        return fraction
    return (x/nod, y/nod)

def collect_fractions(fractions):
    def sum_fractions(fractionOne,fractionTwo):
        x1,y1 = fractionOne
        x2,y2 = fractionTwo
        return simplify_fraction((x1*y2+x2*y1,y1*y2))
    firstfraction = fractions[-1]
    if fractions == []:
        return firstfraction
    fractions.pop()
    firstfraction = simplify_fraction(firstfraction)
    for secondfr in fractions:
        secondfr = simplify_fraction(secondfr)
        firstfraction = sum_fractions(firstfraction,secondfr)
    return firstfraction

def compareTuple(mytuple):
    x,y = mytuple
    return float(x)/float(y)
    
def sort_fractions(fractions):
    fractions.sort(key=compareTuple)
    return fractions

class TestFraction(unittest.TestCase):
    def test_denominator_equal_to_0(self):
        newfraction = simplify_fraction((5,0))
        self.assertTrue(newfraction == (5,0))
    def test_nominator_equal_to_denominator(self):
        newfraction=simplify_fraction((5,5))
        self.assertEqual(newfraction,(1,1))
    def test_startFraction_bigger_than_endFraction(self):
        self.assertTrue((2,4) > simplify_fraction((2,4)))
    def test_calculate_actual(self):
        self.assertTrue((1,2) == simplify_fraction((2,4)))
    def testcollectFractions(self):
        self.assertEqual(collect_fractions([(1, 4), (1, 2)]),(3,4))
        self.assertEqual(collect_fractions([(1, 7), (2, 6)]),(10,21))
    def testEmptyListSorting(self):
        self.assertTrue(sort_fractions([]) == [])
    def testSorting(self):
        self.assertEqual(sort_fractions([(2, 3), (1, 2)]),[(1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]),[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])
if __name__=="__main__":
    unittest.main()