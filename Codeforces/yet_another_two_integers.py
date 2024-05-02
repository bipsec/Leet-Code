def yet_another_two_integers():
    t = int(input())

    while t > 0:
        a, b = map(int, input().split())
        if a > b:
            temp = b
            b = a
            a = temp
        sub = b - a
        div = sub // 10
        mod = sub % 10
        res = div
        if mod > 0:
            res += 1

        print(res)
        t -= 1


yet_another_two_integers()
