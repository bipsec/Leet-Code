class Solution:
    def checkIfExist(self, arr) -> bool:
        arr.sort(key=lambda x: abs(x))

        dupes = []

        for i in range(len(arr)):
            if arr[i] / 2 in dupes:
                return True
            dupes.append(arr[i])

        return False


s = Solution()
print(s.checkIfExist(arr=[10, 2, 5, 3]))
print(s.checkIfExist(arr=[3, 1, 7, 11]))
print(s.checkIfExist(arr=[-10, 12, -20, -8, 15]))
print(s.checkIfExist(arr=[-14, -12, -20, -8, -16]))
print(s.checkIfExist(arr=[-2, 0, 10, -19, 4, 6, -8]))
print(s.checkIfExist(arr=[0, 0]))
print(s.checkIfExist(arr=[-20, 8, -6, -14, 0, -19, 14, 4]))
