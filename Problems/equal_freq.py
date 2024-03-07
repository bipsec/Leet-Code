class Solution:
    def equalFrequency(self, word: str) -> bool:
        dict = {}
        for i in range(len(word)):
            if word[i] not in dict:
                dict[word[i]] = 0
            dict[word[i]] += 1

        
        values = list(dict.values())
        stack = [values[0]]
        # print(stack)

        for index, key in enumerate(dict):
            # print(index, dict[key])
            
            if len(stack) != 0 and index > 0:
                value = dict[key]

                print("Check value", value)

                if value == stack[-1]:
                    stack.pop()
                elif value + 1 == stack[-1]:
                    stack.pop()
                elif value - 1 == stack[-1]:
                    stack.pop()
                stack.append(dict[key])
                
        print(stack)

        return True if len(stack) < 1 else False
    

s = Solution()
print(s.equalFrequency("abcc"))
print(s.equalFrequency("aazz"))
print(s.equalFrequency("aazza"))
print(s.equalFrequency("aazzavmouiawhegvjnaopweduqweuhfbqwevioqwgeygvqwv"))
print(s.equalFrequency("ddaccb"))