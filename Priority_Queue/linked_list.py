class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class Priority_Queue:
    def __init__(self):
        self.start=None
        self.count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority):
        n =Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority <= priority:
                temp=temp.next
            n.next=temp.next
            temp.next = n
        self.count+=1
    def pop(self):
        if not self.is_empty():
            data =self.start.item
            self.start=self.start.next
            self.count-=1
            return data             
        raise IndexError("Priority_Queue is empty")
    def size(self):
        return self.count

pq=Priority_Queue()
pq.push("A",1)
pq.push("E",5)
pq.push("C",3)
pq.push("B",2)
pq.push("D",4)
print("Now the size of Priority_Queue is: ",pq.size())

while not pq.is_empty():
    print("Poped element is: ",pq.pop())
    
print("Now the size of Priority_Queue is: ",pq.size())