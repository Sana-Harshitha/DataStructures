class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_first(self, data):
        self.start = Node(data, self.start)

    def insert_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.start = node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is None:
            return
        node = Node(data, temp.next)
        temp.next = node

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.is_empty():
            return
        self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            return
        if self.start.next is None:
            self.start = None
            return
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_item(self, data):
        if self.is_empty():
            return
        if self.start.item == data:
            self.start = self.start.next
            return
        temp = self.start
        while temp.next is not None and temp.next.item != data:
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next

    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


if __name__ == "__main__":
    my_list = SLL()
    my_list.insert_first(30)
    my_list.insert_first(20)
    my_list.insert_first(10)
    my_list.print_list()
    my_list.insert_last(50)
    my_list.insert_last(60)
    my_list.print_list()
    my_list.insert_after(my_list.search(30), 40)
    my_list.print_list()
    my_list.delete_first()
    my_list.delete_last()
    my_list.print_list()
    my_list.delete_item(30)
    my_list.print_list()

    for i in my_list:
        print(i, end=" ")

