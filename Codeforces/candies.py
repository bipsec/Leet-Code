def distribute_candies():
    t = int(input())

    while t > 0:
        n = int(input())
        x = 3
        while n % x != 0:
            x = (2 * x) + 1
        print(n // x)

        t -= 1


distribute_candies()
