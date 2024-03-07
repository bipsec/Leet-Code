# from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1.sort()
        nums2.sort()

        start = end = 0
        new = 0
        

        while start < len(nums1) and end < len(nums2):
            if nums1[start] < nums2[end]:
                start += 1
            elif nums1[start] > nums2[end]:
                end += 1
            else:
                
                nums1[new] = nums2[end]
                new += 1
                start += 1
                end += 1

        return nums1[0:new]
        
        
        # if len(nums1) > len(nums2):
        #     return self.intersect(nums2, nums1)

        # cnt = Counter(nums1)
        # print(cnt)
        # ans = []
        # for x in nums2:
        #     if cnt[x] > 0:
        #         # print(cnt[x])
        #         ans.append(x)
        #         print(ans)
        #         cnt[x] -= 1
        # return ans


s = Solution()
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(s.intersect([1, 2, 2, 1], [2, 2]))
