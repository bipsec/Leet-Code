def poly_carp_and_coins():
    t = int(input())

    while t > 0:
        n = int(input())
        if n % 3 == 0:
            c1 = n // 3
            c2 = n // 3
        elif (n - 2) % 3 == 0:
            c1 = (n - 2) // 3
            c2 = c1 + 1
        else:
            c1 = (n + 2) // 3
            c2 = c1 - 1
        print(c1, c2, sep=' ')

        t -= 1


poly_carp_and_coins()
