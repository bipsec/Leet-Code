def dhur_eine_ekdome_vallage_na():
    t = int(input())

    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()[:n]))
        m = a[0]
        for j, num in enumerate(a):
            a[j] -= m
        for k in a:
            if a[1] != 0 and a[1] == a[2]:
                print(1)
                break
            if k != 0:
                print(a.index(k) + 1)
                break


# problem ta mojar, vabte icche kortese na ekhn!!! :(

dhur_eine_ekdome_vallage_na()
