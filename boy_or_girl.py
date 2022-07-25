def boy_or_girl():
    name = input()

    name = set(name)

    return "IGNORE HIM!" if len(name) % 2 != 0 else "CHAT WITH HER!"

    # if len(name) % 2 == 0:
    #     print("CHAT WITH HER!")
    # else:
    #     print("IGNORE HIM!")


print(boy_or_girl())
