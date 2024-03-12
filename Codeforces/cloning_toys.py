def clone_toys():
    x , y = list(map(int, input().split()))

    if (x<y-1) or (y<2 and x>0) or (x%2==0 and y%2==0) or (x%2==1 and y%2==1) or (y>=2 and x<1) or (y<1):
        print("NO")
    else:
        print("YES")
    

clone_toys()