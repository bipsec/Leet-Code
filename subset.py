def sub_lists(l):


    # l = [1, 2, 3]

    list = [[]]
    for i in range(len(l)):  # fixed length
        for j in range(len(list)):  # longer
            sub_list = list[j] + [l[i]]
            if sub_list not in l:
                list.append(sub_list)

    print('list =', list)



# driver code
l1 = [1, 2, 3]
print(sub_lists(l1))
