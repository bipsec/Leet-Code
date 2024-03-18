def compare(a, b):
    if abs(a - b) <= 1:
        return True
    else:
        return False


def remove_smallest_from_pair():
    t = int(input())

    while t > 0:
        n = int(input())
        dupes = []
        nums = list(map(int, input().split()[:n]))

        nums.sort()

        start, end = 0, len(nums) - 1

        while start < end:
            if (nums[start] - nums[start+1]) <= 1:
                get_ = compare(nums[start], nums[start+1])
                dupes.append(get_)

            start += 1

        if all(dupes):
            print("YES")
        else:
            print("NO")

        t -= 1


remove_smallest_from_pair()


