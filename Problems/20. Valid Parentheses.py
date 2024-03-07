class Solution:
    def isValid(self, s: str) -> bool:
        
        dupes = []
        
        
        for i in range(0, len(s)-1):
            char = s[i]
            # print(char)
            if char == "(" or char == "{" or char == "[":
                dupes.append(char)
                # print(dupes)
            
            elif len(dupes) == 0:
                return False
            
            elif char == ")" and dupes.pop() != "(" :
                return False
            
            elif char == "}" and dupes.pop() != "{":
                return False
            
            elif char == "]" and dupes.pop() != "[":
                    return False
            
        return len(dupes) == 0


s = Solution()
print(s.isValid("[{()}]"))
