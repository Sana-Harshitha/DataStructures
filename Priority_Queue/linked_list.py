class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class Priority_Queue:
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data, priority):
        node = Node(data, priority)
        if not self.start or priority < self.start.priority:
            node.next = self.start
            self.start = node
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            node.next = temp.next
            temp.next = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority_Queue is empty")
        data = self.start.item
        self.start = self.start.next
        self.count -= 1
        return data

    def size(self):
        return self.count


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

    print("Now the size of Priority_Queue is: ", pq.size())