def sorting_nums():

    input_str = input().split("+")
    input_str = sorted([int(i) for i in input_str])
    return "+".join(str(i) for i in input_str)

print(sorting_nums())