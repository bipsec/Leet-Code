
def wrong_subtraction():

    x, n = list(map(int, input().split()))
    
    while n:

        if x > 1 and x % 10 != 0:
            x -= 1
        else:
            x /= 10
        n -= 1
        
    return int(x)

print(wrong_subtraction())