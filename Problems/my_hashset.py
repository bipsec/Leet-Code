class MyHashSet:

    def __init__(self):
        self.dupes = []

    def add(self, key: int):
        self.dupes.append(key)
        print(f"After adding item: {key}", self.dupes)
        # return self.dupes

    def remove(self, key: int) -> bool:
        try:
            self.dupes = [x for x in self.dupes if x != key]
            return True
        except Exception:
            return False

    def contains(self, key: int) -> bool:
        for item in self.dupes:
            if item == key:
                print(f"After Checking for : {key}", self.dupes)
                return True


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
