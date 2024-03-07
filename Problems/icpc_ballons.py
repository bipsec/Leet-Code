def icpc_baloons():
    n = int(input())

    for i in range(n):
        a = int(input())
        dupes = []
        elm = input()
        for j in range(a):
            dupes.append(elm[j])
        seen = {}

        for k in range(len(dupes)):
            if dupes[k] not in seen:
                seen[dupes[k]] = 2
            else:
                seen[dupes[k]] += 1
        # print(seen)
        res = 0
        for key, value in seen.items():
            res += value
        print(res)


icpc_baloons()
