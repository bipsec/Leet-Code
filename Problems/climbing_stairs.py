"""TOP-DOWN Approach of DP"""


def climb(n):
    result = {}

    if n == 1:
        return 1
    elif n == 2:
        return 2

    if n not in result:
        result[n] = climb(n-1) + climb(n-2)
        # print(f"Storing for {n}", result)
    return result[n]


print(climb(6))


"""BOTTOM-UP Approach of DP"""


def climb_bt_up(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    case1 = 1
    case2 = 2

    for _ in range(2, n):
        result = case1 + case2
        case1 = case2
        case2 = result
    return result


print(climb_bt_up(6))