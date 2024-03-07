# def len_of_words():
n = int(input())
for i in range(n):
    words = str(input())
    # print(words)
    # res = ""

    length = len(words)
    if length <= 10:
        words = words
    else:
        words = words[0] + str(len(words) - 2) + words[-1]
    print(words)


# print(len_of_words())
