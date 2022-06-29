class Queue:
    def __init__(self):
        self.queue = []

    # Add element in queue
    def enqueue(self, item):
        self.queue.append(item)

        return self.display()

    # Remove an element from queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        return self.queue

    # Size of Queue
    def size(self):
        return len(self.queue)


s = Queue()
print(s.enqueue(1))
print(s.enqueue(11))
print(s.enqueue(111))
print(s.enqueue(11111))
print(s.enqueue(111111))
print(s.dequeue())
print(s.display())
print(s.size())
