def round_down_price():
    global diff
    n = int(input())

    for i in range(n):
        a = int(input())
        dupes = []
        for k in range(0, 10):
            val = pow(10, k)
            dupes.append(val)
        # print(dupes)
        for val in dupes:
            if a >= val:
                diff = abs(a - val)
            res = min(diff, a)
        print(res)


round_down_price()