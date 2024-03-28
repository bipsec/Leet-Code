def division_niye_karakari():
    t = int(input())

    while t > 0:

        rating = int(input())

        if rating <= 1399:
            print("Division 4")
        elif 1400 <= rating <= 1599:
            print("Division 3")
        elif 1600 <= rating <= 1899:
            print("Division 2")
        else:
            print("Division 1")

        t -= 1


division_niye_karakari()
