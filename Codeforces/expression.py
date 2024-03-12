def expression():
    a = int(input())
    b = int(input())
    c = int(input())
    nums = []
    for i in range(0, 1):
        nums.append(a + (b*c) )
        nums.append(a*(b+c) )
        nums.append((a*b*c) )
        nums.append((a+b)*c )
        nums.append(a+b+c )
        nums.append((a*b)+c   )
    
 
    print(max(nums))


expression()

