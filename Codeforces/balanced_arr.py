def balance_array():
    t = int(input())

    while t > 0:
        n = int(input())
        if n % 4 == 0:
            print("YES")
            count = 0
            for i in range(2, n + 1, 2):
                print(i, end=" ")
                count = count + i
            tum = 0
            for i in range(1, n - 1, 2):
                print(i, end=" ")
                tum = tum + i
            print(count - tum)

        else:
            print("NO")

        t -= 1


balance_array()

