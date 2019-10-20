class Node(object):
    data = None
    next = None
    prev = None

class Deque:
    curr_node = None
    tail = None

    def list_print(self):
        curr = self.curr_node
        while curr:
            print(curr.data)
            curr = curr.next

    def peek_head(self):
        return self.curr_node.data

    def peek_tail(self):
        if self.tail:
            return self.tail.data
        curr = self.curr_node
        while curr.next:
            curr = curr.next
        return curr.data
    
    def enqueue_head(self, data):
        curr = self.curr_node
        new_node = Node()
        new_node.data = data
        new_node.next = curr
        if curr:
            curr.prev = new_node
        self.curr_node = new_node
    
    def enqueue_tail(self, data):
        new_node = Node()
        new_node.data = data
        if self.tail:
            tail = self.tail
            tail.next = new_node
            new_node.prev = tail
            self.tail = new_node
        else:
            curr = self.curr_node
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            self.tail = new_node
    
    def dequeue_head(self):
        curr = self.curr_node
        temp = curr.next
        temp.prev = None
        self.curr_node = temp
        return curr.data
    
    def dequeue_tail(self):
        if self.tail:
            tail = self.tail
            temp = tail.prev
            temp.next = None
            self.tail = temp
            return tail.data
        curr = self.curr_node
        temp = curr.next
        while temp.next:
            curr = temp
            temp = temp.next
        curr.next = None
        self.tail = curr
        return temp.data


deq = Deque()

deq.enqueue_head(2)
deq.enqueue_head(1)
deq.enqueue_head(0)
deq.enqueue_tail(3)
deq.enqueue_tail(4)
deq.enqueue_tail(5)

deq.list_print()

print('\n')

h = deq.dequeue_head()
t = deq.dequeue_tail()

print(h)
print(t)

print(deq.peek_head())

print(deq.peek_tail())
