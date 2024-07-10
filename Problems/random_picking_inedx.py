import random
from collections import defaultdict
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.dupes = defaultdict(list)

        for i in range(len(nums)):
            self.dupes[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dupes[target])


# Your Solution object will be instantiated and called as such:
nums = [[[1, 2, 3, 3, 3]], [3], [1], [3]]
obj = Solution(nums)
param_1 = obj.pick(3)
param_2 = obj.pick(1)
