def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


array = [23, 14, 64, 13, 64, 23, 86]


def sorting_tuple(tup: tuple):
    tup = sorted(tup)
    return tup


def main():
    print("Bubble Sorting:")
    print("Array before sorting:", array)

    print("Array after sorting:", bubble_sort(array))


if __name__ == '__main__':
    main()
