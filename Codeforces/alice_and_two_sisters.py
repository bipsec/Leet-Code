def ei_j_dunia_kisero_lagia_eto_jotne_goraiyasen_sai():
    t = int(input())

    while t > 0:

        a = int(input())
        ans = 0
        if a % 2 == 0:
            ans = (a // 2) - 1
        elif a % 2 != 0:
            ans = a // 2

        print(ans)

        t -= 1


ei_j_dunia_kisero_lagia_eto_jotne_goraiyasen_sai()
