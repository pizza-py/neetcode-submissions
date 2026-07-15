class MyHashSet:

    def __init__(self):
        self.members = []

    def add(self, key: int) -> None:
        self.members.append(key) if key not in self.members else None
        

    def remove(self, key: int) -> None:
        self.members.remove(key) if key in self.members else None
        

    def contains(self, key: int) -> bool:
        return key in self.members
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)