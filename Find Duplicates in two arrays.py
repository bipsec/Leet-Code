class Solution:
    def findDuplicates(self, nums,val):

        seen = set(val)
        dupes = []

        for i in nums:

            if i in seen:
                dupes.append(i)

            else:
                seen.add(i)
        print(dupes)


s = Solution()
s.findDuplicates([1,2,3,4],[4,5,3,6])
