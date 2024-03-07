def yes():
    n = int(input())

    for i in range(n):
        res = input()

        if res.lower() == "yes":
            print("YES")
        else:
            print("NO")
yes()