def lets_do_2_3_moves():
    t = int(input())
    while t > 0:
        num = int(input())
        if num == 1:
            res = 2

        elif num % 3 != 0:
            res = num // 3 + 1

        else:
            res = num // 3

        print(res)

        t -= 1


lets_do_2_3_moves()
