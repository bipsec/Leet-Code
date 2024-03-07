from math import sqrt
from math import ceil


n = int(input())

for i in range(0, n):
    val = int(input(""))
    number = sqrt(val)
    
    c =1
    
    if(number %2 == 0):
        col = ceil(sqrt(val))
        print(col,c)
    elif (number %2 != 0):
        row = ceil(sqrt(val))
        print(c,row)












# for j in range(0, 9):
#         if (j**2 > val):
#             c = j**2 - val
#             p = val - (j-1)**2
#             if (c < p):
#                 if sqrt(val) % 2 == 0:
#                     col = ceil(sqrt(val))
#                 elif sqrt(val) % 2 != 0:
#                     row = ceil(sqrt(val))





#     if ((sqrt(val)**2 - val) > (sqrt(val))):
#         s = ((sqrt(val)//2)-1)**2
        



#     else:
