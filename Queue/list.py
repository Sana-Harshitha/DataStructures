# queue implementation using list
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    print("rear: ", q1.get_rear(), "front: ", q1.get_front())
    q1.dequeue()
    print("rear: ", q1.get_rear(), "front: ", q1.get_front())
    print("size of queue: ", q1.size())
