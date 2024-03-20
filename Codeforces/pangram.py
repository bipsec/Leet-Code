def vula_jaye_na():
    t = int(input())
    sentence = input()
    sentence = sentence.upper()

    letters = {chr(i+64): i for i in range(1, 27)}
    count = 0

    if len(set(sentence)) < len(letters):
        print("NO")

    else:
        for key, val in letters.items():
            if key in sentence:
                count += 1

        if count == 26:
            print("YES")
        else:
            print("NO")


vula_jaye_na()
