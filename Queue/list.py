#queue implementation using list
class Queue:
    def __init__(self):
        self.items=[]
        self.rear=None
        self.front=None
    def is_empty(self):
        return len(self.items)==None
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
           self.items.pop(0)
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

q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.dequeue()
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.size()
