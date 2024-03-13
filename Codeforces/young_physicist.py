def sum_of_coordinates():
    t = int(input())
    coordinates = []
    x_vals, y_vals, z_vals = 0, 0, 0

    for i in range(t):
        nums = list(map(int, input().split()[:3]))

        coordinates.append(nums)

    for item in coordinates:
        x_vals += item[0]
        y_vals += item[1]
        z_vals += item[2]

        
    if x_vals == y_vals == z_vals == 0:
        print("YES")
    else:
        print("NO")
        



sum_of_coordinates()