def vula_jaye_na():
    t = int(input())
    sentence = input()
    sentence = sentence.upper()

    letters = {chr(i+64): i for i in range(1, 27)}
    count = 0

    print(len(set(sentence)), "|-----|", len(letters))

    if len(set(sentence)) < len(letters):
        print("NO")

    else:
        print("vailuwr")
        for key, val in letters:
            if key in sentence:
                count += 1
    print(count)

    if count == 26:
        print("YES")
    else:
        print("NO")

    # if len(set(sentence)) == len(sentence):
    #     print("YES")
    # else:
    #     print("NO")



vula_jaye_na()