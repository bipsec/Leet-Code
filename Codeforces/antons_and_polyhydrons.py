def shape_edge_calculate():
    t = int(input())
    dupes = {}

    while t > 0:
        vals = input()

        if vals in dupes:
            dupes[vals] += 1
        else:
            dupes[vals] = 1

        t -= 1
    ans = 0

    for key, val in dupes.items():
        if key == "Icosahedron":
            ans += val * 20
        elif key == "Cube":
            ans += val * 6
        elif key == "Cube":
            ans += val * 6
        elif key == "Octahedron":
            ans += val * 8
        elif key == "Dodecahedron":
            ans += val * 12
        elif key == "Tetrahedron":
            ans += val * 4
    

    print(ans)

shape_edge_calculate()