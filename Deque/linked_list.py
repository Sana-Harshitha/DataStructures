class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class Deque:
    def __init__(self):
        self.rear=None
        self.front=None
        self.count=0
    def is_empty(self):
        return self.front == None
    def insert_first(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.prev=n 
        self.front=n
        self.count+=1
    def insert_last(self,data):
        n=Node(data,self.rear,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1
    def deletion_first(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
                self.front.prev=None
                self.count-=1
        else:
            raise IndexError("Queue is empty")
    def deletion_last(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.rear=self.rear.prev
                self.rear.next=None
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


q1=Deque()
q1.insert_first(2)
q1.insert_last(3)
q1.insert_first(1)
q1.insert_last(4)
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
q1.deletion_first()
q1.deletion_last()
print("rear: ",q1.get_rear(),"front: ",q1.get_front())
print("size: ",q1.size())