class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values =None):
        self.head = None
        self.tail = None

        if values is None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return "->".join([str(node) for node in self])

    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def reverse_linkedlist(self):
        prev = None
        current = self.head
        while current is not None:
            following = following.next
            current.next = prev
            prev = current
            current = following
        self.head = prev
        return prev
    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while(current is not None):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

    # def __str__(self):
    #     return "->".join([str(node) for node in self])


s = LinkedList()
print(s.add_node(1))
print(s.add_node(2))
print(s.add_node(3))
print(s.add_node(4))
print(s.head)
print(s.tail)
