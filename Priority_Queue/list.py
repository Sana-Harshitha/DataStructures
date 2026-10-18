class Priority_Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] < priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority_Queue is empty")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    pq = Priority_Queue()
    pq.push("A", 1)
    pq.push("E", 5)
    pq.push("C", 3)
    pq.push("B", 2)
    pq.push("D", 4)
    print("Now the size of Priority_Queue is: ", pq.size())

    while not pq.is_empty():
        print("Popped element is: ", pq.pop())