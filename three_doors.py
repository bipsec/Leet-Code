def open():
    n = int(input())

    for i in range(n):
        a = int(input())
        dupes = list(map(int, input().strip().split()))[:3]
        dupes.append(True)
        x, y, z = 0, 0, 0

        x = dupes[a-1]
        dupes[a-1] = True
        y = dupes[x-1]
        dupes[x-1] = True
        z = dupes[y-1]
        dupes[z-1] = True

        dupes.pop()
        cnt = 0
        for k in range(len(dupes)):
            if dupes[k]:
                cnt += 1
        if cnt == 2:
            print("Yes")
        else:
            print("No")

open()
