class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return not self.start
    def insertion_first(self,data):
        n=Node()
        n.item=data
        if self.is_empty():
            self.start=n
            return
        n.next=self.start 
        self.start.prev=n
        self.start=n
        return
    def insertion_last(self,data):
        n=Node()
        n.item=data
        temp=self.start
        if self.is_empty():
            self.start=n
            return
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
        return
    def search(self, data):
       temp = self.start
       while temp is not None:
         if temp.item == data:
            return temp
         temp = temp.next
       return None  # Return None if the element is not found

    def insertion_after(self,temp,data):
        if temp is None:
          print("Node not found!")
          return
        n=Node()
        n.item=data
        n.next=temp.next
        temp.next.prev=n
        n.prev=temp
        temp.next=n
        return
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        print()
        return
    
    def delete_first(self):
        if self.is_empty():
            return "list is empty!"
        self.start=self.start.next
        if self.start is not None:
            self.start.prev=None 
    def delete_last(self):
        if self.is_empty():
            return "list is empty"
        if self.start.next is None:
            self.start=None
            return
        temp=self.start 
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None
    def delete_item(self,data):
        
        if self.is_empty():
            return print("list is empty")
        if self.start.next is None and self.start.item is data:
            self.start=None  #if only start is present and its item ==data
            return 
        temp=self.start
        if temp.item == data: # no of nodes are present and start item is data
            self.start=temp.next 
            temp.next.prev=None
            return
        while temp.item is not data:
            temp=temp.next
        if temp is None: 
            return print(f"{data} is not found")
        if temp.next is None: # if the data containing node is last one 
            temp.prev.next =None
            return
        temp.prev.next=temp.next
        temp.next.prev=temp.prev

    
my_list=DLL()
my_list.insertion_first(30)
my_list.insertion_first(20)
my_list.insertion_first(10)
my_list.print_list()
my_list.insertion_last(50)
my_list.insertion_last(60)
my_list.print_list()
my_list.insertion_after(my_list.search(30),40)
my_list.print_list()
my_list.delete_first()
my_list.delete_last()
my_list.print_list()
my_list.delete_item(30)
my_list.print_list()