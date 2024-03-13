def check_lucky():
    num = int(input())
    num = str(num)
    count = 0

    for i in range(len(num)):
        if str(num[i]) == "4" or str(num[i]) == "7":
            count += 1
    
    if count == 4 or count == 7:
        print("YES")
    else:
        print("NO")

check_lucky()