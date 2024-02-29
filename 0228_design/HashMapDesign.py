from collections import defaultdict
class MyHashMap:


    def __init__(self):
        self.MyDict = defaultdict()

        
        
    def put(self, key: int, value: int) -> None:
        self.MyDict[key] = value
        


    def get(self, key: int) -> int:
        if key in self.MyDict:
            return self.MyDict[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if self.MyDict[key]:
            del self.MyDict[key]



# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,1)
obj.put(2,3)
param_2 = obj.get(2)
print(param_2)
obj.remove(2)
print(obj.get(2))