class QueueClass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("enqueue to full queue")
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]


# Example usage
if __name__ == "__main__":
    queue = QueueClass(5)
    print(queue.is_empty())  # True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.front())     # 1
    print(queue.dequeue())   # 1
    print(queue.is_full())   # False
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print(queue.is_full())   # True
    print(queue.dequeue())   # 2
    print(queue.front())     # 3
