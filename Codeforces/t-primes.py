import math

def divisor(num):
    res = set()
    sqrt_num = int(math.sqrt(num))
    for x in range(1, sqrt_num + 1):
        if num % x == 0:
            res.add(x)
            if x != num // x:
                res.add(num // x)
    
    return res
 
 
def t_primes():
    t = int(input())
    values = map(int, input().split()[0:t])
 
    for i in values:
        checking_ = [i for i in divisor(i)]
        if len(checking_) == 3:
            print("YES")
        else:
            print("NO")
 
 
t_primes()

# getting TLE for this problem :(
