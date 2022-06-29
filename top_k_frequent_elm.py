class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        def QuickSort(arr):

            elements = len(arr)

            if elements < 2:
                return arr

            current_position = 0

            for i in range(1, elements):
                if arr[i] <= arr[0]:
                    current_position += 1
                    temp = arr[i]
                    arr[i] = arr[current_position]
                    arr[current_position] = temp

            temp = arr[0]
            arr[0] = arr[current_position]
            arr[current_position] = temp

            left = QuickSort(arr[0:current_position])
            right = QuickSort(arr[current_position + 1:elements])

            arr = left + [arr[current_position]] + right

            return arr

        nums = QuickSort(nums)

        if len(nums) == 1:
            return nums

        start, end = 0, len(nums)-1
        dupes = list(set(nums))
        return dupes[0:k]


        while start < end:
            if nums[start] == nums[start+1]:
                nums.remove(nums[start+1])
                # start += 1
            start += 1
        return nums


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
# print(s.topKFrequent([1], 1))
print(s.topKFrequent([1, 1, 2], 2))
print(s.topKFrequent([1, 2], 1))
print(s.topKFrequent([1, 3, 4, 5, 6, 2, 3, 4, 5, 3, 2, 3, 4, 2, 5], 3))
