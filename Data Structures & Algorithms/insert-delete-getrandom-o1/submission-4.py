class RandomizedSet:

    def __init__(self):
        self.randomizedSet = {}
        self.indices = []

    def insert(self, val: int) -> bool:
        if val not in self.randomizedSet:
            self.randomizedSet[val] = len(self.indices)
            self.indices.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.randomizedSet:
            return False
        index = self.randomizedSet[val]
        lastValue = self.indices[-1]
        self.randomizedSet[lastValue] = index
        self.indices[index] = lastValue
        del self.randomizedSet[val]
        self.indices.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.indices)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()