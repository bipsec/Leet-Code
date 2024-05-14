def get_the_range():
    ans = []
    for i in range(1, 100000):
        if i % 3 != 0 and i % 10 != 3:
            ans.append(i)

    return ans


def odd_divisor():
    t = int(input())
    nums = []
    res = get_the_range()
    while t > 0:
        a = int(input())
        print(res[a - 1])
        t -= 1


odd_divisor()
