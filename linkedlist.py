class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.val = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node

    def reverse(self):
        node = self.head
        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)


my_list.reverse()
print(my_list)


