class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insertion_first(self, data):
        node = Node(item=data)
        if self.is_empty():
            self.start = node
            return
        node.next = self.start
        self.start.prev = node
        self.start = node

    def insertion_last(self, data):
        node = Node(item=data)
        if self.is_empty():
            self.start = node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insertion_after(self, temp, data):
        if temp is None:
            print("Node not found!")
            return
        node = Node(temp, data, temp.next)
        if temp.next is not None:
            temp.next.prev = node
        temp.next = node

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.is_empty():
            return "list is empty!"
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None

    def delete_last(self):
        if self.is_empty():
            return "list is empty"
        if self.start.next is None:
            self.start = None
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.prev.next = None

    def delete_item(self, data):
        if self.is_empty():
            return
        if self.start.item == data:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return
        temp = self.start
        while temp is not None and temp.item != data:
            temp = temp.next
        if temp is None:
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next


if __name__ == "__main__":
    my_list = DLL()
    my_list.insertion_first(30)
    my_list.insertion_first(20)
    my_list.insertion_first(10)
    my_list.print_list()
    my_list.insertion_last(50)
    my_list.insertion_last(60)
    my_list.print_list()
    my_list.insertion_after(my_list.search(30), 40)
    my_list.print_list()
    my_list.delete_first()
    my_list.delete_last()
    my_list.print_list()
    my_list.delete_item(30)
    my_list.print_list()