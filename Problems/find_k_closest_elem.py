class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        def compare(num):
            return abs(num - x)

        arr.sort(key=compare)
        closest = arr[:k]

        return sorted(closest)


s = Solution()
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
print(s.findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
print(s.findClosestElements([1, 2, 3, 4, 5, 6, 7, 8, 11, 17, 21], k=11, x=-5))
