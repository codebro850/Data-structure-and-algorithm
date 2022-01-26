class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        current_node = self.head
        if current_node == None:
            print('empty')
        while current_node != None:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print(' ')

    def insert(self, data, position):
        new_node = Node(data)
        if position >= self.length:
            if position > self.length:
                print(
                    "this position is not available so inserting at the end of the list")
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def delete(self, data):
        if self.head == None:
            print('linked list is empty nothing to delete')
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        while (current_node.next != None) and (current_node.next.data != data):
            current_node = current_node.next
        if current_node.next != None:
            current_node.next = current_node.next.next
            if current_node == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print('Given', data, 'value not found')

    def delete_by_position(self, position):
        current_node = self.head
        if position >= self.length:
            if position > self.length:
                print('Position is not present so operation can be performed')
            return
        elif position == 0:
            self.head = current_node.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        else:
            for i in range(position-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return


if __name__ == '__main__':
    mylinkedlist = linkedlist()
    mylinkedlist.append(1)
    mylinkedlist.append(2)
    mylinkedlist.append(4)
    mylinkedlist.append(5)
    mylinkedlist.insert(3, 2)
    mylinkedlist.print_list()
    mylinkedlist.delete(5)
    mylinkedlist.print_list()
    mylinkedlist.prepend(0)
    mylinkedlist.print_list()
    mylinkedlist.prepend(-1)
    mylinkedlist.print_list()
    mylinkedlist.delete(5)
    mylinkedlist.print_list()
    mylinkedlist.delete(9)
    mylinkedlist.delete_by_position(5)
    mylinkedlist.print_list()
