class Solution:
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        
        
        rev = 0
        num = x
        
        while x > 0:
            rev = rev * 10 + x % 10
            x = x// 10
            
        return rev == num


s = Solution()
print(s.isPalindrome(121))
