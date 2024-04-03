def check_me():
    t = int(input())
    res = "codeforces"
    while t > 0:
        char = input()

        if char in res:
            print("YES")
        else:
            print("NO")

        t -= 1


check_me()
