def puzzle_hoye_jabo_ami():
    n, m = map(int, input().split())
    a = list(map(int, input().split()[:m]))

    a.sort()

    x = float('inf')
    for i in range(m - n + 1):
        x = min(x, a[i + n - 1] - a[i])

    print(x)


puzzle_hoye_jabo_ami()
