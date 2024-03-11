def smallest_same_digit_number():
    n = int(input())
    n_str = str(n)
    first_digit = n_str[0]
    k_str = first_digit * len(n_str)
    k = int(k_str)
    while k < n:
        first_digit = str(int(first_digit) + 1)
        k_str = first_digit * len(n_str)
        k = int(k_str)
    return k


result = smallest_same_digit_number()
print(result)
