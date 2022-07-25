def rbs():
    n = int(input())

    for i in range(n):
        dupes = list(map(str, input()))
        stack = []
        cnt = 0
        count = 0
        for j in range(len(dupes)):
            if dupes[j] == "(":
                cnt += 1
            elif dupes[j] == ")":
                cnt -= 1
            elif dupes[j] == "?":
                count += 1
            if 1 - cnt == count:
                count = 0
                cnt = 1
        if cnt == count:
            print("Yes")
        else:
            print("No")


rbs()