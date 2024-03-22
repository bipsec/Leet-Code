class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        number = []
        for i in range(length):
            number.append('0' if nums[i][i] == '1' else '1')
        return ''.join(number)



# matha kharap hoye jay manusher solution dekhle >_<


s = Solution()
print(s.findDifferentBinaryString(nums=["01", "10"]))
print(s.findDifferentBinaryString(nums=["00", "01"]))
print(s.findDifferentBinaryString(nums=["111", "011", "001"]))
