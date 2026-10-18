class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Cll:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def print_list(self):
        if self.is_empty():
            print("list is empty")
            return
        temp = self.last.next
        while temp is not self.last:
            print(temp.item, end=" ")
            temp = temp.next
        print(temp.item)

    def insert_first(self, data=None):
        node = Node(data)
        if self.is_empty():
            node.next = node
            self.last = node
            return
        node.next = self.last.next
        self.last.next = node

    def insert_last(self, data=None):
        node = Node(data)
        if self.is_empty():
            node.next = node
            self.last = node
            return
        node.next = self.last.next
        self.last.next = node
        self.last = node

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp is not self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            node = Node(data, temp.next)
            temp.next = node
            if temp == self.last:
                self.last = node

    def delete_first(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
            return
        self.last.next = self.last.next.next

    def delete_last(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
            return
        temp = self.last.next
        while temp.next is not self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp

    def delete_item(self, data):
        if self.is_empty():
            return
        if self.last.item == data:
            if self.last.next == self.last:
                self.last = None
                return
            self.delete_last()
            return
        temp = self.last.next
        while temp is not self.last and temp.item != data:
            temp = temp.next
        if temp is self.last and temp.item != data:
            return
        if temp.next == self.last and self.last.item == data:
            self.last = temp
        temp.next = temp.next.next

    def __iter__(self):
        if self.last is None:
            return Cll_Iterator(None)
        return Cll_Iterator(self.last.next)


class Cll_Iterator:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data


if __name__ == "__main__":
    circular = Cll()
    print("insert_first")
    circular.insert_first(40)
    circular.print_list()
    print("insert_last")
    circular.insert_last(60)
    circular.print_list()
    circular.insert_after(circular.search(40), 50)
    circular.print_list()
    circular.insert_after(circular.search(60), 70)
    circular.print_list()
    for value in circular:
        print(value, end="_")
