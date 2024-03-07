# class Solution:
#     def countSmaller(self, nums):
#         res = []

#         start, end = 1, len(nums)

#         for i in range(len(nums)):
#             count = 0
#             while start < end:
#                 if nums[i] > nums[start]:
#                     count += 1
#                 start += 1
#             start = i + 1
#             res.append(count)
#         return res
    
class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        
        # Normalize the nums array to start from 1
        normalized_nums = {val: idx + 1 for idx, val in enumerate(sorted(set(nums)))}
        
        # Initialize BIT
        bit = [0] * (len(normalized_nums) + 1)
        
        def update(index):
            while index < len(bit):
                bit[index] += 1
                index += index & -index
        
        def query(index):
            count = 0
            while index > 0:
                count += bit[index]
                index -= index & -index
            return count
        
        result = []
        for num in reversed(nums):
            idx = normalized_nums[num]
            result.append(query(idx - 1))
            update(idx)
        
        return reversed(result)

# Example usage:
solution = Solution()
nums = [5, 2, 6, 1]
print(solution.countSmaller(nums))  # Output should be [2, 1, 1, 0]






s = Solution()
print(s.countSmaller(nums = [5,2,6,1]))
print(s.countSmaller(nums = [-1]))
print(s.countSmaller(nums = [-1,-1]))