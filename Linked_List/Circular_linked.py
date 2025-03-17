class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Cll:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return not self.last
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp is not self.last:
              print(temp.item,end=" ")
              temp=temp.next
            print(temp.item)
            return
        print("list is empty")
        
        
    def insert_first(self,data=None):
        node=Node()
        node.item=data
        if self.is_empty():
            node.next=node
            self.last=node
            return
        node.next=self.last.next
        self.last.next=node
    def insert_last(self,data=None):
        node=Node()
        node.item=data
        if self.is_empty():
            node.next=node
            self.last=node
            return
        node.next=self.last.next
        self.last.next=node
        self.last=node
    def search(self,data):
        if not self.is_empty():
            temp=self.last.next
            while temp is not self.last:
               if temp.item == data:
                   return temp
               temp=temp.next
            if temp.item == data:
                   return temp
            return None
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            node=Node(data,temp.next)
            temp.next=node
            if temp==self.last:
                self.last=node
    def delete_first(self):
        if self.is_empty():
            return print("list is empty")
        if self.last.next==self.last:
            self.last=None
            return
        self.last.next=self.last.next.next
    def delete_last(self):
        if self.is_empty():
            return print("list is empty")
        if self.last.next==self.last:
            self.last=None
            return
        temp=self.last.next
        while temp.next is not self.last:
            temp=temp.next
        temp.next=self.last.next
        self.last=temp

    def delete_item(self,data):
        temp=self.last.next
        if self.last.item == data:
            if temp == self.last:
                self.last=None
                return
            return self.delete_last()
        else:
            if temp.item == data:
                return self.delete_first()
        while temp is not self.last:
            if temp.next.item == data:
                temp.next=temp.next.next
            temp=temp.next
    def __iter__(self):  # to make Cll as an iterater
        if self.last==None:
            return Cll_Iterator(None)
        return Cll_Iterator(self.last.next)
class Cll_Iterator:
    def __init__(self,start):
        self.start=start
        self.current=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else :
            self.count = 1
        data = self.current.item
        self.current=self.current.next
        return data
         
          

            
        

        

    

list=Cll()
print("insert_first")
list.insert_first(40)
list.print_list()
print("insert_last")
list.insert_last(60)
list.print_list()
list.insert_after(list.search(40),50)
list.print_list()
list.insert_after(list.search(60),70)
list.print_list()
# list.delete_first()
# list.print_list()
# list.delete_last()
# list.print_list()
# list.delete_item(60)
# list.print_list()
# list.delete_item(50)
# list.print_list()
for i in list:
    print(i,end="_")
