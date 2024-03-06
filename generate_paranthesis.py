class Solution:    
    def generate_(self, output, open, close, pairs):
        ans = []
        if open == pairs and close == pairs:
            ans.append(output)
        else:
            if open<pairs:
                self.generate_(output+'(', open+1, close, pairs)
            if close<open:
                self.generate_(output+')', open, close+1, pairs)
        return ans

    def generateParenthesis(self, n: int):
        
        combinations = set()
        if n == 1:
            combinations.add('()')
        else:
            previous_sets = self.generateParenthesis(n - 1)
            for previous_set in previous_sets:
                for i, c in enumerate(previous_set):
                    temp_string = "{}(){}".format(previous_set[:i+1], previous_set[i+1:])
                    combinations.add(temp_string)

        return list(combinations)
    


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))
# print(s.foo('', 0, 0, 3))