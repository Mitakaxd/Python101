import json
import sys
import random

class Car:
    def __init__(self,car,model,max_speed):
        self.__car = car
        self.__model = model
        self.__max_speed = max_speed
    def __str__(self):
        return str(self.__car) + " " + str(self.__model) + " Top speed: " + str(self.__max_speed)
    def __dict__(self):
        d = {}
        d["car"] = self.__car
        d["model"] = self.__model
        d["max_speed"] = self.__max_speed
        return d
    @property
    def max_speed(self):
        return self.__max_speed
    
class Driver:
    def __init__(self, name, car):
        self.__car = car
        self.__name = name
    def __str__(self):
        return "Driver name: " + self.__name + " with the magnifficent: " + str(self.__car)
    def __dict__(self):
        d = {}
        d["car"] = self.__car.__dict__
        d["name"] = self.__name
        return d
    @property
    def name(self):
        return self.__name
    
    @property
    def speed(self):
        return self.__car.max_speed
    
class Race:
    def results(self):
        points = [8,6,4]
        for driver in self.__drivers:
            if random.random() > self.__crash_chance: #chance to crash
                if len(points) > 0 : # if first places arent taken
                    #print(driver.name, "- ", points[0])
                    self.__standings[driver.name] = points[0] 
                    points = points[1:]  #pop first elemnt of points
                else:
                    self.__standings[driver.name] = 0
            else:
                self.__standings[driver.name] = "Unfortunately " + str(driver) + " crashed"
        for driver_name,result in self.__standings.items():
            if isinstance(result,int):
                print(driver_name, " - ", result)
                #first print finished participants
        for driver, result in self.__standings.items():
            if not isinstance(result,int):
                print(result)

    def write_to_Json_results(self):
        with open('results.json', 'a') as f:
            print(json.dumps(self.__standings), file = f)
    def __init__(self, drivers,crash_chance):
        self.__drivers = sorted(drivers,key=lambda driver:driver.speed)
        self.__crash_chance = crash_chance
        self.__standings = {}

class Championship:
    def __init__(self, name, races_count):
        self.__name = name
        self.__races_count = races_count
        drivers = self.__readDriversfromJson()
        #initialized participants and tournament
        #make races count races
        for r in range(races_count+1):
            curRace = Race(drivers,random.random())
            print("Race number: ", r)
            curRace.results()
            curRace.write_to_Json_results()
            print('===============')
    def __readDriversfromJson(self):
        with open("cardrivers.json") as DriversFile:
            drivers = json.load(DriversFile)
            arrofDrivers = [Driver(driver["name"],Car(driver["car"],driver["model"],driver["max_speed"])) for driver in drivers["people"]]
        return arrofDrivers
    @classmethod
    def top3(cls):
        with open('results.json') as result_file:
            results = [json.loads(line) for line in result_file]
            drivers = results[0].keys()
            drivers_results = dict.fromkeys(drivers,0)
            for race_results in results:
                for driver, points in race_results.items():
                    if isinstance(points,int):
                        drivers_results[driver] += points
            print(sorted(drivers_results.items(),key = lambda driver: driver[1],reverse = True )[:3])

def main():
    if sys.argv[1] == "standings":
        Championship.top3()
    elif sys.argv[1] == "start":
        curChampionship = Championship(sys.argv[2],int(sys.argv[3]))


if __name__ == '__main__':
    main()