class StackClass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("push to full stack")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.stack[-1]


# Example usage
if __name__ == "__main__":
    stack = StackClass(5)
    print(stack.is_empty())  # True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.top())       # 3
    print(stack.pop())       # 3
    print(stack.is_full())   # False
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.is_full())   # True
