# cook your dish here
def fair():
    n = int(input())

    while n:
        dupes = list(map(int, (input().strip().split())))[:2]

        if dupes[-1] >= dupes[-2] + 1:
            print("YES")
        else:
            print("NO")
        n -= 1

fair()