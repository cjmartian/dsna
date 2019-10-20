class Node(object):
    data = None
    next = None
    prev = None

class DoublyLinkedList:
    curr_node = None
    tail_node = None

    def list_print(self):
        curr = self.curr_node
        while curr:
            print(curr.data)
            curr = curr.next

    def search(self, data):
        curr = self.curr_node
        i = 0
        while curr:
            if curr.data == data:
                print(i)
            curr = curr.next
            i += 1

    def insert(self, index, data):
        curr = self.curr_node
        temp = curr.next
        new_node = Node()
        new_node.data = data
        i = 1
        while i != index:
            curr = temp
            temp = temp.next
            i += 1
        curr.next = new_node
        new_node.prev = curr
        new_node.next = temp
        temp.prev = curr

    def insert_head(self, data):
        new_node = Node()
        new_node.data = data
        if self.curr_node:
            curr = self.curr_node
            new_node.next = curr
            curr.prev = new_node
            self.curr_node = new_node
        else:
            self.curr_node = new_node
            self.tail_node = new_node

    def insert_tail(self, data):
        new_node = Node()
        new_node.data = data
        if self.tail_node:
            tail  = self.tail_node
            tail.next = new_node
            new_node.prev = tail
            self.tail_node = new_node
        elif self.curr_node:
            curr = self.curr_node
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            self.tail_node = new_node
        else:
            self.curr_node = new_node
            self.tail_node = new_node

    def remove(self, index):
        prev = None
        curr = self.curr_node
        temp = curr.next
        i = 0
        while i != index:
            prev = curr
            curr = temp
            temp = temp.next
            i += 1
        prev.next = temp
        temp.prev = prev

    def remove_head(self):
        curr = self.curr_node.next
        curr.prev = None
        self.curr_node = curr

    def remove_tail(self):
        if self.tail_node:
            temp = self.tail_node.prev
            self.tail_node = temp
        else:
            curr = self.curr_node
            temp = curr.next
            while temp.next:
                curr = temp
                temp = temp.next
            curr.next = None
            temp.prev = None
            self.tail_node = curr


dll = DoublyLinkedList()

dll.insert_head(3)
dll.insert_head(1)
dll.insert_head(0)
dll.insert(2, 2)
dll.insert_tail(4)
dll.insert_tail(5)
dll.insert_tail(6)


dll.list_print()

print('\n')

dll.remove_head()

dll.remove(2)

dll.remove_tail()

dll.list_print()


dll.search(2)
