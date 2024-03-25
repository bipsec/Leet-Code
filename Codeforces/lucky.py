def if_god_is_testing_me_then_okay_I_am_fine_with_it():
    t = int(input())

    while t > 0:

        get_that_shit = input()

        count = 0
        for i in range(len(get_that_shit)):
            if i <= 2:
                count += int(get_that_shit[i])
            else:
                count -= int(get_that_shit[i])

        if count == 0:
            print("YES")
        else:
            print("NO")

        t -= 1


if_god_is_testing_me_then_okay_I_am_fine_with_it()
