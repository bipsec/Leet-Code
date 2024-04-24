def food_for_animals():
    t = int(input())

    while t > 0:

        a, b, c, x, y = map(int, input().split())
        dogs = x - a
        cats = y - b

        if dogs <= 0 and cats <= 0:
            print("YES")
        else:
            if dogs < 0:
                dogs = 0
            if cats < 0:
                cats = 0

            left = dogs + cats
            if left <= c:
                print("YES")
            else:
                print("NO")

        t -= 1


food_for_animals()
