def gas_stations(distance, tank_size, stations):
    currentDistance=tank_size
    result=[]
    while currentDistance<distance:
        closest=max([x for x in stations if x<currentDistance]) #filter out bigger elements, get max of them 
        result.append(closest)
        currentDistance=closest+tank_size # station + full reservoir
    return result

# print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))


def is_number_balanced(number):
    string=str(number)
    lst=[int(num) for num in string]
    mid=int(len(lst)/2)
    lst1=lst[0:mid]
    if len(lst)%2==1:
        mid+=1
    lst2=lst[mid : len(lst)]
    return sum(lst1)==sum(lst2)
# print(is_number_balanced(9))
# print(is_number_balanced(4518))
# print(is_number_balanced(28471))
# print(is_number_balanced(1238033))

def increasing_or_decreasing(seq):
    increasing_seq = sorted(list(set(seq))) # if there are repating elements we return false
    decreasing_seq = sorted(list(set(seq)),reverse=True)
    if increasing_seq == seq:
        return "UP"
    if decreasing_seq == seq:
        return "DOWN"
    return False

# print(increasing_or_decreasing([1,2,3,4,5]))
# print(increasing_or_decreasing([5,6,-10]))
# print(increasing_or_decreasing([1,1,1,1]))
# print(increasing_or_decreasing([9,8,7,6]))

#SUM NUMBERS IN STRING

# Sum all numbers in a given string

def sum_of_numbers(input_string):
    new_string=''
    for ch in input_string:
        if not ch.isdigit():
            ch = ' '
        new_string += ch
    return sum([int(num) for num in new_string.split(' ') if num != ''])

# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
#print(sum_of_numbers("11110"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))

def get_largest_palindrome(start_num):
    def isPalyndrome(n):
         return n == int(str(n)[::-1])
    for num in range(start_num-1, 1, -1):
        if isPalyndrome(num):
            return num

# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))




# Birthday Ranges
# Implement a function that calculates how many people are 
#born in a range of start and end date(end is included in the range).

def birthday_ranges(birthdays, ranges):
    result=[]
    for start,end in ranges:
        result.append(len(list(filter(lambda birthday: birthday>=start and birthday<=end, birthdays))))
    return result



# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))





#Nokia
nokia_dict={1:'',
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
            }
#     If you press 1, the next letter is going to be capitalized
#     If you press 0, this will insert a single white-space
#     If you press a number and wait for a few seconds, the special breaking number -1 enters the sequence. This is the way to write different letters from only one keypad!
def numbers_to_message(digits):
    #import group from week01 old school
    def group(lst):
        groups = []
        current_group = []
        for elem in lst:
            if len(current_group) == 0 or elem == current_group[-1]:
                current_group.append(elem)
            else:
                groups.append(current_group)
                current_group = [elem]
        groups.append(current_group)
        return groups

    result_str = ''
    nextCapital = False
    for digit_group in group(digits):
        if digit_group[0] == 0:
            result_str += ' '
            continue
        if digit_group[0] == 1:
            nextCapital = True
            continue
        if digit_group[0] == -1:
            continue
        if nextCapital:
            result_str += nokia_dict[digit_group[0]][(len(digit_group)-1)%len(nokia_dict[digit_group[0]])].upper()
            nextCapital = False
        else:
            result_str += nokia_dict[digit_group[0]][(len(digit_group)-1)%len(nokia_dict[digit_group[0]]) ]
    return result_str


# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))

# print(numbers_to_message([2, 2, 2, 2]))
# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))



def message_to_numbers(message):
    reverse_nokia_dict = {}
    for k,v in nokia_dict.items():
        for idx, ch in enumerate(v):
            reverse_nokia_dict[ch] = str(k) * (idx+1)
    result_list = []
    for letter in message:
        if letter.isupper():
            result_list += [1] + list(reverse_nokia_dict[letter.lower()])
            continue
        if letter == ' ':
            result_list += [0]
            continue
        if len(result_list)>0 and reverse_nokia_dict[letter][0] == result_list[-1]:
            result_list += [-1]
        result_list += list(reverse_nokia_dict[letter])
    return result_list

# print(message_to_numbers("abc"))
# print(message_to_numbers("a"))
# print(message_to_numbers("Ivo e Panda"))
# print(message_to_numbers("aabbcc"))



# Elevator Trips

# Create a function, that calculates the amount of trips an elevator must do to leave the people on their floors. The input parameters are:

#     people_weight - a list of integers, which represents the weight of people
#     people_floors - a list of integers, which represents the floor, on which a person must go
#     elevator_floors - the number of the elevator floors
#     max_people - the maximum amount of people, that can be in the elevator at the same time
#     max_weight - the maximum weight, that the elevator can handle

#todo
def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    sorted_people = sorted(zip(people_weight,people_floors),key=lambda: 

print(elevator_trips([], [], 5, 2, 200))
print(elevator_trips([40, 50], [], 5, 2, 200))
print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))




