from Linked_List.single_linked import SLL

class Stack(SLL):
    def __init__(self):
        super().__init__()  
        self.count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        self.insert_first(data)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item  
            self.delete_first()
            self.count -= 1
            return data  
        else:
            raise IndexError("Stack underflow")  

    def peek(self):
        if not self.is_empty():
            return self.start.item  
        else:
            raise IndexError("Stack underflow")  

    def size(self):
        return self.count  

# Example usage
stack = Stack()
stack.push(2)
stack.push(5)
stack.push(4)
print("Top item is:", stack.peek())
print("Size of stack is:", stack.size())
print("Popped item is:", stack.pop())
print("Top item is:", stack.peek())
print("Size of stack is:", stack.size())