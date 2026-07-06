#Dictionnary and every thing in O(1)

class MyHashSet:

    def __init__(self):
        self.myset = {} #Dict 

    def add(self, key: int) -> None:
        self.myset[key] = True 

    def remove(self, key: int) -> None:
        if key in self.myset:
            del self.myset[key]
        
    def contains(self, key: int) -> bool:
        return key in self.myset
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)