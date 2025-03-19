# queue implementaion using linked list
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n 
        self.count+=1
    
    def dequeue(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            self.count-=1
        else:
            raise IndexError("Queue is empty")
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty")
    def size(self):
        return self.count


q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.dequeue()
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
print("size of Queue: ",q1.size())