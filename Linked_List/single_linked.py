class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=None
    def is_empty(self):
        return not self.start
    def insert_first(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_last(self,data):
        n=Node(data)
        if  self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if(temp.item==data):
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        print()
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None: # 0 Nodes
            pass
        elif self.start.next is None: # 1 Node
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None 
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start 
            while temp.next.item is not data:
                temp=temp.next
            temp.next=temp.next.next
    def __iter__(self):
        return SLLIterator(self.start)
        
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current :
            raise StopIteration
        data=self.current.item
        self.current=self.current.next 
        return data
    
# my_list=SLL()
# my_list.insert_first(30)
# my_list.insert_first(20)
# my_list.insert_first(10)
# my_list.print_list()
# my_list.insert_last(50)
# my_list.insert_last(60)
# my_list.print_list()
# my_list.insert_after(my_list.search(30),40)
# my_list.print_list()
# my_list.delete_first()
# my_list.delete_last()
# my_list.print_list()
# my_list.delete_item(30)
# my_list.print_list()

# #we converted my_list into iterable object
# for i in my_list:
#     print(i, end=" ")        

