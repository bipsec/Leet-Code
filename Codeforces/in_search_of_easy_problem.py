def kire_eita_kono_problem_hoilo():
    t = int(input())
    nums = list(map(int, input().split()[:t]))

    for item in nums:
        if item == 1:
            print("HARD")
            break
    else:
        print("EASY")


kire_eita_kono_problem_hoilo()
