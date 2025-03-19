#queue implementation using list
class Deque:
    def __init__(self):
        self.items=[]
        self.rear=None
        self.front=None
    def is_empty(self):
        return len(self.items)==None
    def insert_first(self,data):
        self.items.insert(0,data)
    def insert_last(self,data):
        self.items.append(data)
    def deletion_first(self):
        if not self.is_empty():
           self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
    def deletion_last(self):
        if not self.is_empty():
           self.items.pop()
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    def size(self):
        return print("size of queue: ",len(self.items))

q1=Deque()
q1.insert_first(2)
q1.insert_last(3)
q1.insert_first(1)
q1.insert_last(4)
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.deletion_first()
q1.deletion_last()
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.size()
