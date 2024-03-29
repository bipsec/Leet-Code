def morse_code():
    encoded_str = input()
    res = ""

    i = 0
    while i < len(encoded_str):
        if encoded_str[i] == ".":
            res += "0"
            i += 1
        elif encoded_str[i] == "-":
            if i + 1 < len(encoded_str) and encoded_str[i + 1] == ".":
                res += "1"
                i += 2
            elif i + 1 < len(encoded_str) and encoded_str[i + 1] == "-":
                res += "2"
                i += 2

    print(res)


morse_code()
