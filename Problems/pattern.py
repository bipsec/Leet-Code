# def pattern():
#     a = int(input())
#     for i in range(1, a + 1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
#
#
# # pattern()
#
# def pattern2():
#     b = int(input())
#     for i in range(0, b + 1):
#         for j in range(1, b - i + 1):
#             print("*", end=" ")
#         print()
#
#
# # pattern2()
#
#
# def pattern3():
#     b = int(input())
#     for i in range(1, b + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()


# pattern3()


def pattern4():
    b = int(input())
    for row in range(0, b * 2):
        if row > b:
            col = 2 * b - row
            for j in range(0, col):
                print("*", end=" ")
        else:
            col = row
            for j in range(0, col):
                print("*", end=" ")
        print()


# pattern4()

def pattern5():
    b = int(input())
    for row in range(0, b * 2):

        col = row if row <= b else (2 * b - row)
        space = b - col
        for s in range(0, space):
            print(end=" ")

        for j in range(0, col):
            print("*", end=" ")

        print()


pattern5()
