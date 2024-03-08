class Solution:
    def maxFrequencyElements(self, nums) -> int:
        
        dupes = {}
        # for num in nums:
        #     if num in dupes:
        #         dupes[num] += 1
        #     else:
        #         dupes[num] = 1

        
        for num in nums:
            dupes[num] = dupes.get(num, 0) + 1
        # print(dupes)

        # got to learn new things to insert freq countitng in dictionary
        
        max_freq = max(dupes.values())
        count_max_freq = list(dupes.values()).count(max_freq)

        return max_freq * count_max_freq
     

s = Solution()
print(s.maxFrequencyElements(nums = [1,2,2,3,1,4]))
print(s.maxFrequencyElements(nums = [1,2,3,4,5]))
print(s.maxFrequencyElements(nums = [1,2,3,4,5,6,7,8,3,4,2,3,4]))
print(s.maxFrequencyElements([19,19,19,20,19,8,19]))
        