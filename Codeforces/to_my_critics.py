def dhur_hala_simple_jog_er_problem_dise():
    t = int(input())

    while t > 0:

        a, b, c = map(int, input().split())

        if (a + b) >= 10 or (b + c) >= 10 or (a + c) >= 10:
            print("YES")
        else:
            print("NO")

        t -= 1


dhur_hala_simple_jog_er_problem_dise()
