def distance(a, n):
    m = 3 * n
    m = m // 2
    left = a[:m]
    right = a[m:]
    print(left, right)
    left.sort()
    right.sort()
    max_left = 0
    min_right = right[-1] + right[-2]
    for i in range(len(left)-1, -1, -1):
        left_sum = (left[i-1] + left[i])
        max_left = max(max_left, left_sum)
    # print(max_left)
    for i in range(len(right)-1, -1, -1):
        # print(i)
        right_sum = (right[i-1] + right[i])
        min_right = min(min_right, right_sum)
    # print(min_right)
    return max_left - min_right

# Use priority queue :((((((((((((


print(distance([1, 3, 5, 2, 1, 1], 2))
print(distance([1, 1, 5, 3, 7, 7], 2))
print(distance([1, 1, 4, 5, 2, 6, 9, 1, 11, 4, 5, 3], 4))
# print(distance([47, 67], 100))
