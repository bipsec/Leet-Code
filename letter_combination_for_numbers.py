class Solution:
    def letterCombinations(self, digits: str):

        if len(digits) == 0:
            return []
        numsDict = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6": 'mno',
            "7": 'pqrs',
            "8": 'tuv',
            "9": 'wxyz'
        }
        combination = []

        def traverse(comb, next_item):
            if not next_item:
                combination.append(comb)
                return

            for item in numsDict[next_item[0]]:
                traverse(comb + item, next_item[1:])

        traverse("", digits)
        return combination


s = Solution()
print(s.letterCombinations(digits="23"))
print(s.letterCombinations(digits="234"))
print(s.letterCombinations(digits=""))
