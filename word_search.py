class Solution:
    def exist(self, board, word) -> bool:
        res = []
        vals = ""
        for i in board:
            res += i
        vals = "".join(res)
        result = []
        ans = ""
        for i in range(len(word)):
            if word[i] in vals:
                result.append(word[i])
                vals.replace(word[i], " ")
        print(res)
        ans += "".join(result)
        if ans != word:
            return False
        return True


s = Solution()
# print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
# print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
# print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
print(s.exist([["a", "b"], ["c", "d"]], "abcd"))
