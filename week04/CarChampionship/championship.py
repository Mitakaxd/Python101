import json
import sys
import random

class Car:
    def __init__(self,car,model,max_speed):
        self.car=car
        self.model=model
        self.max_speed=max_speed
    def __str__(self):
        return str(self.car)+" "+str(self.model)+" Top speed: "+str(self.max_speed)
    def __dict__(self):
        d={}
        d["car"]=car
        d["model"]=model
        d["max_speed"]=max_speed
        return d
class Driver:
    def __init__(self,name,car,cur_points=0):
        self.car=car
        self.name=name
        self.cur_points=cur_points
    def __str__(self):
        return "Driver name: "+self.name+" with the magnifficent: "+str(self.car)
    def __dict__(self):
        d={}
        d["car"]=dict(self.car)
        d["name"]=name
        d["cur_points"]=cur_points
        return d
class Race:
    def start(self):
        print(self.drivers)
        points=[8,6,4,0]
        for idx,driver in enumerate(sorted(self.drivers,key=lambda driver:getattr(driver.car,"max_speed"))) :
            if random.random()>self.crash_chance:
                if idx<3:
                    driver.cur_points+=points[idx]
                    print(str(driver),"- ",points[idx])
                else:
                    print(str(driver), " - 0")
            else:
                print("Unfortunately ",str(driver),"crashed")
    def __dict__(self):
        d={}
        for driver in drivers:
            d["drivers"]
        d["drivers"]
    def __init__(self, drivers,crash_chance):
        self.drivers=drivers
        self.crash_chance=crash_chance
        self.start()
class Championship:
    def __init__(self,name,races_count):
        self.name=name
        self.races_count=races_count
        drivers=self.readDriversfromJson()
        #initialized participants and tournament
        #make races count races
        for r in range(races_count+1):
            curRace=Race(drivers,random.random())
            with open("results.json") as result:
                json.dump(curRace,result)
                del curRace

    def readDriversfromJson(self):
        with open("cardrivers.json") as DriversFile:
            drivers=json.load(DriversFile)
            arrofDrivers=[Driver(driver["name"],Car(driver["car"],driver["model"],driver["max_speed"])) for driver in drivers["people"]]
        return arrofDrivers
    def top3(self):
        with open("results.json") as result:
            results=json.load(result)
            #to finish


def main():
    if sys.argv[1]=="standings":
        printresultJson()
    elif sys.argv[1]=="start":
        curChampionship=Championship(sys.argv[2],int(sys.argv[3]))


if __name__ == '__main__':
    main()