class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
           return super().pop()
        else:
            raise IndexError("Stack is empty") 
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")  

    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No Attribute 'insert' in Stack")
    
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
s1.insert(1,10) #Attribute Error