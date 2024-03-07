class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        # R = int(input("Enter number of rows: "))
        # C = int(input("Enter number of columns: "))
        m = len(mat)
        n = len(mat[0])

        matrix = []
        new_mat = []

        for i in range(m):
            a = []
            for j in range(n):
                a.append(mat[j])
            new_mat.append(a)
        # print(matrix)

        for i in range(m):
            for j in range(n):
                # new_mat.append(mat[i][j])
                print(new_mat[i][j], end=" ")
            print()

        # for i in range(r):
        #     b = []
        #     for j in range(c):
        #         b.append(mat[j])
        #     new_mat.append(b)
        # # print(matrix)
        #
        # for i in range(r):
        #     for j in range(c):
        #         # new_mat.append(mat[i][j])
        #         print(new_mat[i][j], end=" ")
        #     print()


s = Solution()
print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
