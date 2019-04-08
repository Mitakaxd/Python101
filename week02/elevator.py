from itertools import groupby
def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    #take people while.. 
    #group, get count trips +1, repeat
    def group_and_count(lst_of_floors):
        return len(list(groupby(lst_of_floors)))+1
    count_trips = 0
    sum_of_weight = 0
    count_people = 0
    trip = []
    for idx in range(len(people_floors)):
        # print(idx)
        sum_of_weight += people_weight[idx]
        count_people += 1
        if count_people > max_people or sum_of_weight > max_weight:
            # print(trip)
            count_trips += group_and_count(trip)
            count_people = 0
            sum_of_weight = 0
            trip = [people_floors[idx]]
        else:
            trip.append(people_floors[idx])
    count_trips += group_and_count(trip)
    return count_trips

def main():
    print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))
    print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))

if __name__ == '__main__':
    main()