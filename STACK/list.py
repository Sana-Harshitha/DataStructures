class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            return True
        return False
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
           return self.items.pop()
        else:
            raise IndexError("Stack is empty") 
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")  

    def size(self):
        return len(self.items)
    
s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
print(s1.peek())
print(s1.pop())
print(s1.peek())
s1.push(20)
s1.push(21)
s1.push(22)
print(s1.size())