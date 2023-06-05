class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        return "null"

    def pop(self) -> None:
        self.stack.pop()
        return "null"

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-1))
print(obj.push(-2))
print(obj.push(-3))
print(obj.pop())
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
