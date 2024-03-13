def chess_game():
    t = int(input())
    count = 0
    countD = 0
    res = input()

    for i in res:
        if i == "A":
            count += 1
        elif i == "D":
            countD += 1
    
    if count > countD:
        print("Anton")
    elif count == countD:
        print("Friendship")
    else:
        print("Danik")

    
chess_game()