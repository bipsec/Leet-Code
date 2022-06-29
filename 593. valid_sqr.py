class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:

        if p1 == p2 == p3 == p4: return False
    
        res = [self.distance(p1, p2), self.distance(p1, p4),
                self.distance(p2, p3), self.distance(p3, p4),
                self.distance(p1, p3), self.distance(p2, p4)]
        
        res = sorted(res)
        
        
        if res[0] == res[1] == res[2] == res[3]:
            if res[4] == res[5]:
                return True
        return False

    def distance(self, p1, p2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        return abs(x ** 2 + y ** 2)


s = Solution()
print(s.validSquare([0,0],[1,0],[0,1],[1,12]))

