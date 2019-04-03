#Sum of all digits of a number
def sum_of_digits(n):
    sumDigits = 0
    n = abs(n)
    while n>0:
        sumDigits += n%10
        n= n//10
    return sumDigits

#Turn a number into a list of digits
def to_digits(n):
    lst = []
    while n>0:
        lst = [n%10] + lst
        n = n//10
    return lst

#Turn a list of digits into a number
def to_number(lst):
    n=len(lst)-1
    num=0
    for digit in lst:
        num+=digit*(10**n)
        n-=1
    return num

# print(to_number([1,2,3]))
# print(to_number([9,9,9,9,9]))
# print (to_number([1,2,3,0,2,3]))
# print(to_number([2,1, 2, 3,3]))

#Implement a function fact_digits(n),
#that takes an integer and returns the sum of the factorials of each digit of n.
def fact_digits(n):
    digits=to_digits(n)
    sumofFact=0
    for digit in digits:
        num=1
        for i in range(1,digit+1):  
            num=num*i
        sumofFact+=num
    return sumofFact

# print(fact_digits(111))
# print(fact_digits(145))
# print(fact_digits(999))

# Implement a function, called palindrome(obj), which takes 
# an object (could be anything) and 
# checks if it's string representation is a palindrome.
def palindrome(obj):
    obj=str(obj)
    i=0
    maxlen=len(obj)-1
    while i<maxlen//2+1:
        if obj[i]!=obj[maxlen-i]:
                return False
        i+=1
    return True



# print(palindrome(123))
# print(palindrome("kapak"))
# print(palindrome("baba"))

#Vowels in a string

# Implement a function, called count_vowels(str),
#  which returns the count of all vowels in the string str.
def count_vowels(str):
    count=0
    for letter in str:
        if letter in "AEIOUYaeiouy":
            count+=1
    return count

# print(count_vowels("Python"))
# print(count_vowels("Theistareykjarbunga"))
# print(count_vowels("grrrrgh!"))
# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
# print(count_vowels("A nice day to code!"))


#Implement a funcion, called char_histogram(string), which takes a string and returns a dictionary,
#  where each key is a  character from string and its value 
#  is the number of occurrences of that char in string.

def char_histogram(string):
    dict = {}
    for ch in string:
        if ch in dict.keys():
            dict[ch]+=1
        else:
            dict[ch]=1
    return dict

# print(char_histogram("Python!"))
# print(char_histogram("AAAAaaa!!!"))


#Sum Numbers in Matrix
def sum_matrix(m):
    return sum ([sum(lst) for lst in m])

#NaN Expand
def nan_expand(n):
    return ' '.join(['Not a' for count in range(n)]+['Nan'] )

# print(nan_expand(2))
# print(nan_expand(3))


# Implement a function, called prime_factorization(n), which takes an integer and
#  returns a list of tuples (pi, ai) that is the result of the factorization.
def prime_factorization(n):
    return [(prime, GetTimes(n,prime)) for prime in range(2,n//2+1) if IsPrime(prime) if GetTimes(n,prime)>0]+[(n,1) for num in [1] if IsPrime(n)]

def IsPrime(toCheck):
    for i in range(2, toCheck//2+1):
        if(toCheck%i==0):
            return False
    return True
def GetTimes(num,prime):
    counter=0
    while num%prime==0:
        counter+=1
        num=num//prime
    return counter


# print(prime_factorization(10))
# print(prime_factorization(14))
# print(prime_factorization(356))

# print(prime_factorization(89))
# print(prime_factorization(1000))

def group(lst):
    groups=[]
    current_group = []
    for elem in lst:
        if len(current_group)==0 or elem == current_group[-1]:
            current_group.append(elem)
        else:
            groups.append(current_group)
            current_group = [elem]
    groups.append(current_group)
    return groups


assert group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
assert group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]

def max_consecutive(items):
    return max([len(lst) for lst in group(items)])

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))

