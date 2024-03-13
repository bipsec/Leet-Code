def tram_capacity():
    
    t = int(input())

    maxNum = float("-inf")
    getIn = 0
    exited = 0
    while t > 0:
        a, b = list(map(int, input().split()))
        getIn += b
        exited += a

        val = getIn-exited

        if val > maxNum:
            maxNum = val 
        t -= 1

    print(maxNum)


tram_capacity()