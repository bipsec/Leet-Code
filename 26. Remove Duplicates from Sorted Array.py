class Solution:
    def removeDuplicates(self, nums):

        seen = set(nums)

        lenNum = len(nums);
        lenSeen = len(seen);
        nums = [];
        for x in seen:
            nums.append(x)
        print(nums)
        for i in range(lenNum-lenSeen):
            nums.append(0)
        

        # p =len(dupes)
        # l = k - len(dupes)
        # s = "_"
        
        # dupes += l * [s] 
        
        # # print(f"{p}, {dupes}")
        # print(dupes)
            
        



s = Solution()
s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
