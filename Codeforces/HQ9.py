def is_it_a_joke():
    command = input().strip()

    for char in command:
        if char in "HQ9":
            print("YES")
            return

    print("NO")


is_it_a_joke()


# def hq9_plus(program):
#     for char in program:
#         if char in "HQ9":
#             return "YES"
#     return "NO"
#
# # Example usage
# program_input = input().strip()
# print(hq9_plus(program_input))
