class Solution:
    def exist(self, board, word):
        self.board, self.word = board, word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, i, j, k):

        if not self.board[i][j] == self.word[k]:
            return False

        if len(self.word) == k + 1:
            return True

        self.board[i][j] = "#"

        for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= a < len(self.board) and 0 <= b < len(self.board[0])):
                continue
            if self.dfs(a, b, k + 1):
                return True

        self.board[i][j] = self.word[k]
        return False


# not mine :( -- have some confusion about the solution


s = Solution()
# print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
# print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
print(s.exist([["a", "b"], ["c", "d"]], "abcd"))
