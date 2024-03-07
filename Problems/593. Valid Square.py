class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        

        def distance(p1, p2):
            x = p1[0] - p2[0]
            y = p1[1] - p2[1]
            return x ** 2 + y ** 2
        

        def compare(p1, p2):
            if p1[0] < p2[0]:
                return -1
            elif p2[0] < p1[0]:
                return 1
            else:
                if p1[1] < p2[1]:
                    return -1
                elif p2[1] < p1[1]:
                    return 1
                else:
                    return 0

        def sortedArray(arr):
            for i in range(4):
                for j in range(i+1, 4):
                    if compare(arr[i], arr[j]) == -1:
                        pass
                    elif compare(arr[i], arr[j]) == 1:
                        temp = arr[i]
                        arr[i] = arr[j]
                        arr[j] = temp
                    else:
                        pass
            return arr

        arr = [p1, p2, p3, p4]

        arr = sortedArray(arr)
        # print(arr)

        val = distance(arr[0], arr[3])
        res = distance(arr[1], arr[2])
        side_1 = distance(arr[0], arr[1])
        side_2 = distance(arr[0], arr[2])
        
        return val == res and side_1 == side_2 and val != 0 and side_1 != 0



    # x = (p1[0]+p2[0]+p3[0]+p4[0])/4
    # y = (p1[1]+p2[1]+p3[1]+p4[1])/4
    # side_1 = self.distance(p1,p2)
    # side_2 = self.distance(p1, p4)
    # diag_1 = self.distance(p1, p3)
        # side_4 = self.distance(p2, p3)
        # side_5 = self.distance(p2, p4)
        # diag_2 = self.distance(p3, p4)
        
        # print(x, y)
        # if side_1 == side_2 == side_4 == side_5:
        #     if diag_1 == diag_2:
        #         return True
        #     return False
        # return False

       

s = Solution()
print(s.validSquare([0, 0], [5, 0], [5, 4], [0, 4]))
print(s.validSquare([1, 1],
                    [3, 5],
                    [5, 3],
                    [7, 7]))
