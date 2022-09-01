import collections
from collections import deque

class SmallestInfiniteSet:

    nums = collections.deque()

    def __init__(self):
        for i in range(1, 1000+1):
            self.nums.append(i)
        return None

    def popSmallest(self) -> int:
        val = self.nums.popleft()
        return val

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.appendleft(num)
        return None



# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
# print(obj)
param_1 = obj.popSmallest()
print(param_1)
param_1 = obj.popSmallest()
print(param_1)
print(obj.addBack(3))
# obj
param_1 = obj.popSmallest()
print(param_1)
print(obj.addBack(2))

param_1 = obj.popSmallest()
print(param_1)
param_1 = obj.popSmallest()
print(param_1)

# ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
# [[],[],[],[3],[],[2],[],[]]