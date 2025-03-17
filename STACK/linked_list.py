class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,start=None):
        self.start=start
        self.count=0
    def is_empty(self):
        return self.start==None
    def push(self,data):
            n=Node(data,self.start)
            self.start=n
            self.count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.count-=1
            print("Popped item is: ",data)
        else:
            return print("Stack underflow")
    def peek(self):
        if not self.is_empty():
            return print("top item is: ",self.start.item)
        return print("Stack underflow")
    def size(self):
        return print("No of items in stack is: ",self.count)


stack=Stack()
stack.push(2)
stack.push(5)
stack.push(4)
stack.peek()
stack.size()
stack.pop()
stack.peek()
stack.size()