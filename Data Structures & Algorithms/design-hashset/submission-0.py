class MyHashSet:

    def __init__(self):
        self.capacity=1000
        self.buckets=[[] for i in range(self.capacity)]
        

    def add(self, key: int) -> None:
        idx=key%self.capacity
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)
        

    def remove(self, key: int) -> None:
        idx=key%self.capacity
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
        

    def contains(self, key: int) -> bool:
        idx = key % self.capacity
        return key in self.buckets[idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)