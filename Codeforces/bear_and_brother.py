def bear_and_brother():
    a , b = list(map(int, input().split()))

    count = 0
    while True:
        a *= 3
        b *= 2
        count += 1
        if a > b:
            break
    print(count)
    
bear_and_brother()