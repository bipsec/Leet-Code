def friends_and_candies():
    t = int(input())

    while t > 0:
        n = int(input())
        x = 3
        while n % x != 0:
            x = (2 * x) + 1

            ans = n // x

            print(ans)

        t -= 1


friends_and_candies()
