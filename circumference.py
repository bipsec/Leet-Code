import math
class Solution:
    def fun1(self, a,b,c,d, e,f):
        # 
        # a,b,c,d,e,f = map(int, (input()).split())

        pi = 3.141592653589793
        h = min((e-a), (c-a), (e-c))
        k = min((f-b), (d-b), (f-d))
        r = math.sqrt(c**2 + d**2)
        circle = 2 * pi * r
        return circle


s = Solution()
# print(s.fun1(1, 2, 3, 4, 5, 6))
print(s.fun1(0.0, - 0.5, 0.5, 0.0, 0.0, 0.5))
print(s.fun1(0.0, 0.0, 0.0, 1.0, 1.0, 1.0))
print(s.fun1(5.0 ,5.0 ,5.0 ,7.0 ,4.0 ,6.0))
print(s.fun1(0.0 ,0.0, - 1.0, 7.0, 7.0, 7.0))
print(s.fun1(50.0, 50.0, 50.0, 70.0, 40.0, 60.0))
print(s.fun1(0.0 ,0.0, 10.0, 0.0, 20.0, 1.0))
print(s.fun1(0.0, - 500000.0, 500000.0, 0.0, 0.0, 500000.0))
