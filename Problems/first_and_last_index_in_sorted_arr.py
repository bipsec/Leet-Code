class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0\
                or nums[0] > target\
                or nums[-1] < target:
            return [-1, -1]

        def find_start(arr, val):
            if arr[0] == val:
                return 0
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < val:
                    left = mid + 1
                elif arr[mid] == val and arr[mid - 1] < val:
                    return mid
                else:
                    right = mid - 1
            return -1

        def find_end(arr, val):
            if arr[-1] == val:
                return len(arr) - 1
            left, right = 0, len(arr) - 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > val:
                    right = mid - 1
                elif arr[mid] == val and arr[mid + 1] > val:
                    return mid
                else:
                    left = mid + 1
            return -1

        start = find_start(nums, target)
        end = find_end(nums, target)
        return [start, end]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 6))
print(s.searchRange([1], 1))
print(s.searchRange([], 0))
print(s.searchRange([0], 0))
print(s.searchRange([1,3], 1))
print(s.searchRange([3, 3, 3], 3))
