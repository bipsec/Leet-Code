class MyCalendar:

    def __init__(self):
        self.dupes = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.dupes:
            if i < end and start < j:
                return False
        self.dupes.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10, 20)
print(param_1)
param_2 = obj.book(15, 25)
print(param_2)
param_3 = obj.book(20, 30)
print(param_3)
