class Solution:
    def removeDuplicateLetters(self, s):
        
        seen = set(s)
        
        seen = sorted(seen, key=str.lower)
        
        s ="".join(list(map(str, seen)))
        
        if s.islower():
            print('"{}"'.format(s))
        
        
       
    

p = Solution()
p.removeDuplicateLetters("bcabc")
