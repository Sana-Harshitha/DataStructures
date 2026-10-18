class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Stack:
    def __init__(self, start=None):
        self.start = start
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data):
        node = Node(data, self.start)
        self.start = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        data = self.start.item
        self.start = self.start.next
        self.count -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.start.item

    def size(self):
        return self.count


if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())