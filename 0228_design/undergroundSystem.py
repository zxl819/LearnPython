from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.costumers = defaultdict()
        self.timeCost = defaultdict()


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.costumers[id] = [stationName, t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        timeSum = t - self.costumers[id][1] 
        transport = self.costumers[id][0] + " " + stationName
        if transport in self.timeCost:
            self.timeCost[transport][1] += 1
            self.timeCost[transport][0] += timeSum
            
        else:
            self.timeCost[transport] = [timeSum, 1] 


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trans = startStation + " " + endStation
        if trans in self.timeCost:
            averTime = float(self.timeCost[trans][0] / self.timeCost[trans][1])
        return averTime 



# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
print(obj.checkIn(45, "Leyton", 3))
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
print(obj.getAverageTime("Leyton","Waterloo"))