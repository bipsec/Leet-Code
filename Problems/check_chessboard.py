class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        chars = ["a", "b", "c", "d", "e", "f", "g", "h"]

        chessboard = {}

        for i in range(1, 9):
            for j in range(len(chars)):
                key = chars[j] + str(i)
                chessboard[key] = (i + j) % 2 == 0

        return chessboard[coordinate1] == chessboard[coordinate2]



s = Solution()
# print(s.checkTwoChessboards(coordinate1="a1", coordinate2="c3"))
# print(s.checkTwoChessboards(coordinate1="a1", coordinate2="h3"))
# print(s.checkTwoChessboards(coordinate1="a7", coordinate2="a6"))
print(s.checkTwoChessboards(coordinate1="c2", coordinate2="g4"))
