class Solution:
    def containsDuplicate(self, nums):
        l = []
        val = set()

        for i in nums:
            if i in val:
                l.append(i)
                # print(l)   
            else:
                val.add(i)
                # print(val)
            
        return False if len(l) ==0 else True
                
                


s = Solution()
print(s.containsDuplicate([1,2,3,1]))
