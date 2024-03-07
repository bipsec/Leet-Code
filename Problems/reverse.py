def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    result = []
    seen = ""
    for i in range(len(sentence)):
        if sentence[i].islower():
            seen += sentence[i].upper()
        else:
            seen += sentence[i].lower()
    seen = seen.split()

    for i in range(len(seen)-1, -1, -1):
        result.append(seen[i])

    return " ".join(i for i in result)



print(reverse_words_order_and_swap_cases("rUns doG"))
