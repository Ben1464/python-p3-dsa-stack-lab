class Stack:
    def __init__(self, items=None, capacity=None):
        # Initialize the stack with a list of items and an optional capacity
        self.items = items if items is not None else []
        self.capacity = capacity

    def push(self, item):
        # Add item to stack if it's not full
        if self.capacity is None or len(self.items) < self.capacity:
            self.items.append(item)

    def pop(self):
        # Remove and return the top item from stack if not empty, otherwise return None
        if not self.isEmpty():
            return self.items.pop()
        return None

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def full(self):
        # Check if the stack is full
        return self.capacity is not None and len(self.items) == self.capacity

    def search(self, item):
        # Return the distance from the top of the stack
        if item in self.items:
            return len(self.items) - self.items.index(item) - 1
        return -1
