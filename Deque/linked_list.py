class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def is_empty(self):
        return self.front is None

    def insert_first(self, data):
        node = Node(data, None, self.front)
        if self.is_empty():
            self.rear = node
        else:
            self.front.prev = node
        self.front = node
        self.count += 1

    def insert_last(self, data):
        node = Node(data, self.rear, None)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.count += 1

    def deletion_first(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.front.item
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.count -= 1
        return data

    def deletion_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.rear.item
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.count -= 1
        return data

    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.item

    def size(self):
        return self.count


if __name__ == "__main__":
    q1 = Deque()
    q1.insert_first(2)
    q1.insert_last(3)
    q1.insert_first(1)
    q1.insert_last(4)
    print("rear: ", q1.get_rear(), "front: ", q1.get_front())
    q1.deletion_first()
    q1.deletion_last()
    print("rear: ", q1.get_rear(), "front: ", q1.get_front())
    print("size: ", q1.size())