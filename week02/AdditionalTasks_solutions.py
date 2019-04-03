
#Anagrams
from math import sqrt,ceil

def anagram(word, word2):
    dict={}
    for ch in word:
        try:
            dict[ch]+=1
        except Exception:
            dict[ch]=1
    dict2={}
    for ch in word2:
        try:
            dict2[ch]+=1
        except Exception:
            dict2[ch]=1
    return dict==dict2
#Test Examples:
# print(anagram("boro","robo"))
# print(anagram("BRADE","BEARD"))




# Goldbach Conjecture
# Implement a function, called goldbach(n) which returns a list of tuples,
# that is the goldbach conjecture for the given number n.


def goldbach(n):
    def isPrime(num):
        for k in range(2,ceil(sqrt(num))+1):
            if num % k == 0 and k < num:
                return False
        return True
    return [(num, n-num) for num in range(2,n//2+1) if isPrime(num) and isPrime(n-num)]
# Test examples
# print(goldbach(4))
# print(goldbach(6))
# print(goldbach(8))
# print(goldbach(10))
# print(goldbach(100))





def is_credit_card_valid(number):
    number_to_list = [int(ch) for ch in str(number)]

    if len(number_to_list) % 2 == 0:
        return False

    number_to_list_reversed = number_to_list [::-1]
    for idx, digit in enumerate(number_to_list_reversed):
        if idx % 2 == 1:
            if digit*2 >= 10:
                number_to_list_reversed[idx] = digit*2 - 9
            else:
                number_to_list_reversed[idx] = digit*2
    return sum(number_to_list_reversed) % 10 == 0
            



# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398715))
