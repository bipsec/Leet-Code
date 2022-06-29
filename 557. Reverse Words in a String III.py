class Solution:
    def reverseString(self, s):

        s = s.split()

        start, end = 0, len(s)-1
        for i in range(0,len(s)):
                       
            while start < end:
                s[i][start], s[i][end] = s[i][end], s[i][start]
                start += 1
                end -= 1

        return ' '.join(s)


s = Solution()
print(s.reverseString("hello this is nice"))
