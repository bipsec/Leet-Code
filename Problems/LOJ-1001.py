n = int(input())

for i in range(0,n):
    val  = int(input(""))
    
    if val <10:
        a = val
        b = 0
        print(a,b)

    elif val == 10:
        a = 0
        b = val
        print(a,b)
    elif val >10:
        a = val-10
        b = val -a
        print(b, a)
    
