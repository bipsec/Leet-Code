from collections import deque
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1: return []

        changed.sort()
        res, queue = deque(), deque()

        for num in changed:
            if queue and num == queue[0] * 2:
                res.append(queue.popleft())
            else:
                queue.append(num)

        return [] if queue else res


s = Solution()
print(s.findOriginalArray(changed=[1, 3, 4, 2, 6, 8]))
print(s.findOriginalArray(changed=[6, 3, 0, 1]))
print(s.findOriginalArray(changed=[1, 2, 2, 1]))
print(s.findOriginalArray(changed=[0, 0, 0, 0]))
print(s.findOriginalArray(changed=[0, 0, 3]))
