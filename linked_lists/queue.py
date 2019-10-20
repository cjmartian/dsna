class Node(object):
    data = None
    next = None

class Queue:
    curr_node = None

    def list_print(self):
        curr = self.curr_node
        while curr:
            print(curr.data)
            curr = curr.next


    def peek(self):
        return self.curr_node.data


    def enqueue(self, data):
        curr = self.curr_node
        new_node = Node()
        new_node.data = data
        if self.curr_node is None:
            self.curr_node = new_node
            return
        while curr:
            curr = curr.next


    def dequeue(self):
        curr = self.curr_node
        self.curr_node = curr.next
        return curr.data


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)

qu.list_print()

de = qu.dequeue()

print(de)

de = qu.dequeue()

print(de)
print(qu.peek())
