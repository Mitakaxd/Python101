import unittest
#to split polynome into monomial instances
#to improve abstractions
import sys
class Molynome:
    @classmethod
    def __check_int(cls,s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
    def __str__(self):
        return "(const {}, power {}".format(self.__const,self.__power)
    @property
    def derivative(self):
        if self.__power == 0:
            return '0'
        if self.__power == 1:
            return str(self.__const)
        result = str(self.__power * self.__const) + "*x"
        if self.__power > 2:
            result +="^"+str(self.__power-1)
        return result

    def __init__(self,const=0,power=0):
        self.__const = const
        self.__power = power

    @classmethod
    def from_string(cls,string):
        if '^' in string:
            molynome_split = string.split('^')
            power = int(molynome_split[-1])
            #variable = molynome_split[0][-1] #last symbol
            if '*' in string:
                const=string.split('*')[0]
            else:
                const = 1
        elif '*' in string:
            const = string.split('*')[0]
            power = 1
        elif cls.__check_int(string):
            const = string
            power = 0
        else:
            power = 1
            const = 1
        return cls(int(const),power)

    def get_power(self):
        return self.__power

    def __add__(self,other):
        if self.__power != other.__power:
            raise ValueError("Illegal sum")
        self.__const += other.__const
        return self

class Polynome:
    def __init__(self,fromstring):
        self.__molynomes=[]
        self.__fromstring(fromstring)
        self.__molynomes.sort(key=lambda molynome:molynome.get_power(),reverse=True)
    def __str__(self):
        output=""
        for molynome in self.__molynomes:
            output += str(molynome)
        return output
    def __fromstring(self,string):
        molynomes_strings = string.split('+')
        for molynome_string in molynomes_strings:
            self.__molynomes.append(Molynome.from_string(molynome_string))

    def derivative(self):
        result_list=[]
        sum_of_molynomes_with_same_power = self.__molynomes[0]

        for idx,molynome in enumerate(self.__molynomes[1:]):
            if sum_of_molynomes_with_same_power.get_power() != molynome.get_power():
                result_list.append(sum_of_molynomes_with_same_power.derivative)
                sum_of_molynomes_with_same_power = molynome
            else:
                sum_of_molynomes_with_same_power += molynome
        if result_list == [] or sum_of_molynomes_with_same_power.derivative!='0':
            result_list.append(sum_of_molynomes_with_same_power.derivative)
        return "f(x)`= "+' + '.join(result_list)
                





class TestPolynome(unittest.TestCase):
    def test_check_molynome(self):
        moly=Molynome.from_string("5")
        self.assertEqual(moly.derivative,"0")
    def test_check_molynome2(self):
        moly=Molynome.from_string("6*x^2")
        self.assertEqual(moly.derivative,"12*x")
    def test_checkExample_without_x_expected_0(self):
        poly=Polynome("1")
        self.assertEqual(poly.derivative(),"f(x)`= 0")

    def test_check_example_with_only_x_expected_1(self):
        poly=Polynome("x")
        self.assertEqual(poly.derivative(),"f(x)`= 1")
    def test_checkExample_with_power_going_to_one(self):
        poly=Polynome("3*x^2")
        self.assertEqual(poly.derivative(),"f(x)`= 6*x")

    def test_checkExample_with_multiple_monomials(self):
        poly=Polynome("2*x^3+x")
        self.assertEqual(poly.derivative(),"f(x)`= 6*x^2 + 1")
    def test_checkExample_with_no_constant_before_x(self):
        poly=Polynome("x^4+10*x^3")
        self.assertEqual(poly.derivative(),"f(x)`= 4*x^3 + 30*x^2")
    def test_checkExample_with_different_order_and(self):
        poly=Polynome("1+x^2")
        self.assertEqual(poly.derivative(),"f(x)`= 2*x")




if __name__ == '__main__':
    unittest.main()




