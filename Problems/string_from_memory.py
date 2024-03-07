def memory():
    n = int(input())

    for i in range(n):
        words = input()

        nums = set()
        c = 0
        res = 1
        for k in range(len(words)):
            nums.add(words[k])
            if len(nums) == 4:
                nums.clear()
                res += 1
            nums.add(words[k])
        print(res)




memory()
