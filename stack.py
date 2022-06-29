def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items to the stack
def push(stack, item):
    stack.append(item)
    print("Pushed items: " + item)


# Removing an element from stack
def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()


stack = create_stack()
print("Popped item: " + pop(stack))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))
push(stack, str(6))
print("Popped item: " + pop(stack))
print("Stack after popping item: " + str(stack))

