
class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return "->".join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple_node(self, values):
        for value in values:
            self.add_node(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def __str__(self):
        return "->".join([str(node) for node in self])

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return prev



    def sort_list(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.value > index.value:
                        current.value, index.value = index.value, current.value
                    index = index.next
                    current = current.next
        return s.head

    # def printList(self):
    #     temp = self.head
    #     while (temp):
    #         print(str(temp.value) + " ", end="")
    #         temp = temp.next


s = LinkedList()
print(s.add_node(1))
print(s.add_node(2))
print(s.add_node(3))
print(s.add_node(4))
# print(s.head)
# print(s.tail)
# print(s.add_multiple_node([2, 4, 3]))
# print(s.add_multiple_node([5, 6, 4]))
# print(s.add_multiple_node([5, 6, 4]))
# print(s.head)
print(s.reverse())
# print(s.sort_list(s.head))
# print(s.printList())
# print(s.tail)
# print(s.values)
# print(s.__str__())
# print(s.__len__())
# print(s.add_multiple_node(1))




