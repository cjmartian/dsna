class Node(object):
    data = None
    next = None

class LinkedList:
    curr_node = None

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
                print(index)
                break
            i += 1

    def insert(self, index, data):
        # doesn't handle if inserting at position 0
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
        new_node.next = temp

    def insert_head(self, data):
        new_node = Node()
        new_node.data = data
        if self.curr_node:
            curr = self.curr_node
            new_node.next = curr
        self.curr_node = new_node


    def insert_tail(self, data):
        curr = self.curr_node
        new_node = Node()
        new_node.data = data
        while curr.next:
            curr = curr.next
        curr.next = new_node

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

    def remove_head(self):
        curr = self.curr_node
        temp = curr.next
        curr.next = None
        self.curr_node = temp

    def remove_tail(self):
        curr = self.curr_node
        temp = curr.next
        while temp.next:
            curr = temp
            temp = temp.next
        curr.next = None


ll = LinkedList()

ll.insert_head(2)
ll.insert_head(1)
ll.insert_head(0)
ll.insert(3, 3)
ll.insert_tail(4)
ll.insert_tail(5)
ll.insert_tail(6)

ll.list_print()

print('\n')

ll.remove_head()

ll.remove_tail()

ll.remove(2)

ll.list_print()
