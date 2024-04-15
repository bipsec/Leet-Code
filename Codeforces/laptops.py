def make_alex_happy():
    t = int(input())
    ans = []
    for i in range(t):
        a, b = map(int, input().split())
        ans.append([a, b])
    ans.sort()
    maxAnswer = 0
    for i in range(t):
        a, b = ans[i]
        if b <= maxAnswer:
            return "Happy Alex"
        maxAnswer = b
    return "Poor Alex"


print(make_alex_happy())

