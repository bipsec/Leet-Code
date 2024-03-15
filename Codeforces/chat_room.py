def chat_room():
    get_input = input()

    start, end = 0, len(get_input) - 1
    target = "hello"
    stack = ""
    i = 0
    while start <= end:
        if len(stack) != len(target):
            if get_input[start] == target[i]:
                # print(get_input[start], "------------", target[i])
                stack += get_input[start]
                i += 1
        start += 1

    # print(stack)

    if stack == target:
        print("YES")
    else:
        print("NO")


chat_room()
