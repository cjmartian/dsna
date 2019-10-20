class Node(object):
    data = None
    next = None

class Stack:
    curr_node = None

    def stack_print(self):
        node = self.curr_node
        while node:
            print(node.data)
            node = node.next

    def push(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.curr_node
        self.curr_node = new_node


    def peek(self):
        return self.curr_node.data


    def pop(self):
        curr = self.curr_node
        self.curr_node  = curr.next
        return curr.data


st = Stack()
st.push(0)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)


st.stack_print()


print(st.peek())

a = st.pop()
print(a)


st.stack_print()
