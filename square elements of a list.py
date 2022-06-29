class Solution:
    def sortedSquares(self, s):
        length = len(s)
        output = [0] * length

        start = 0
        end = len(s) -1

        for i in range(end, -1, -1):

            if (abs(s[end])) > (abs(s[start])):
                val = s[end]
                end -=1
            else:
                val = s[start]
                start +=1
            
            output[i] = val*val
            
        return output
    

s = Solution()
print(s.sortedSquares([-5, -4, -3, -2, -1]))
