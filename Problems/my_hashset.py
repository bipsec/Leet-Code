class MyHashSet:

    def __init__(self):
        self.dupes = []

    def add(self, key: int):
        self.dupes.append(key)

    def remove(self, key: int) -> bool:
        self.dupes = [x for x in self.dupes if x != key]

    def contains(self, key: int) -> bool:
        return key in self.dupes


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [], [1], [2], [1], [3], [2], [2], [2], [2]
s = MyHashSet()
print(s.add(1))
print(s.add(2))
print(s.contains(1))
print(s.contains(3))
print(s.add(2))
print(s.contains(2))
print(s.remove(2))
print(s.contains(2))
