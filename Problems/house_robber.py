def rob(n):

    if n == 0:
        return house[0]
    elif n == 1:
        return max(house[0], house[1])
    result = {}

    if n not in result:
        result[n] = max((rob(n-2) + house[n], rob(n-1)))
    return result[n]


house = [10, 60, 80, 20, 8]

print(rob(len(house)-1))


def rob_bt_up(house):

    if len(house) == 1:
        return house[0]
    elif len(house) == 2:
        return max(house[0], house[1])

    case1 = house[0]
    case2 = max(house[0], house[1])

    for n in range(2, len(house)):
        result = max(case1 + house[n], case2)
        case1 = case2
        case2 = result
    return result


house = [10, 60, 80, 20, 8]
print(rob_bt_up(house))
