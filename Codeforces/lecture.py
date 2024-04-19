def lecture():
    n, m = map(int, input().split())
    dupes = {}
    for _ in range(m):
        a, b = input().split()
        dupes[a] = b
    words = input().split()
    result = []
    for word in words:
        if len(dupes.get(word, "")) < len(word):
            result.append(dupes.get(word, ""))
        else:
            result.append(word)
    print(" ".join(result))


lecture()
