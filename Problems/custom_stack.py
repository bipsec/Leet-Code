class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:

        if self.stack:
            self.inc[min(k, len(self.stack)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(3)
obj.push(2)
obj.push(1)
obj.push(2)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_1 = obj.pop()
obj.increment(2, 100)
obj.increment(5, 100)
obj.increment(2, 100)
