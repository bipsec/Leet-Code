words = str(input())

res = words[0].upper()
res += "".join(i for i in words)[1:]

print(res)