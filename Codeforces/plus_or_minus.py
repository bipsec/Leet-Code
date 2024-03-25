def life_is_having_fun_with_me():
    t = int(input())

    while t > 0:

        a, b, c = list(map(int, input().split()[:3]))

        if a + b == c:
            print("+")
        else:
            print("-")

        t -= 1


life_is_having_fun_with_me()
