class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) < 3:
            return False

        left = 0
        right = len(arr) - 1
        while right > left:
            if arr[left] < arr[left+1]:
                left = left + 1
            elif arr[right] < arr[right-1]:
                right = right - 1
            else:
                return False
        if left == right and left != (len(arr) - 1) and right != 0:
            return True
        else:
            return False


s = Solution()
print(s.validMountainArray(arr=[0, 3, 2, 1]))
print(s.validMountainArray(arr=[3, 5, 5]))
print(s.validMountainArray(arr=[2, 1]))
