class Node:
    data = None

    def __init__(self, data):
        self.data = data


class HashMap:
    del_symbol = -1

    def __init__(self, init_size):
        self.init_size = init_size
        self.store = [None for _ in range(self.init_size)]
        self.size = 0
        self.limit = 15

    def _hash(self, v, n):
        index = v % self.init_size + (n * n)
        while index > self.init_size - 1:
                index = index % self.init_size
        return index

    def list_print(self):
        for i in self.store:
            if i:
                if i == self.del_symbol:
                    print(i)
                else:
                    print(i.data)
            else:
                print(i)

    def search(self, v):
        start = 0
        while start < self.limit:
            index = self._hash(v, start)
            if self.store[index]:
                node = self.store[index]
                if node.data == v:
                    return index
            else:
                return "Hash Table does not include {}".format(v)
            start += 1

    def insert(self, v):
        start = 0
        new_node = Node(v)
        while start < self.limit:
            index = self._hash(v, start)
            if not self.store[index] or self.store[index] == self.del_symbol:
                self.store[index] = new_node
                return index
            start += 1
    
    def remove(self, v):
        start = 0
        while start < self.limit:
            index = self._hash(v, start)
            if self.store[index]:
                node = self.store[index]
                if node.data == v:
                    self.store[index] = self.del_symbol
                    return index
                start += 1
            break
        return "Hash Table does not include {}".format(v)
        
hm = HashMap(7)

hm.insert(7)    # h(7) = 7 % 7 + (0 * 0) = 0

hm.insert(14)   # h(14) = 14 % 7 + (0 * 0) = 0 (taken)
                # 14 % 7 + (1 * 1) = 1 

hm.insert(21)   # h(21) = 21 % 7 + (0 * 0) = 0 (taken)
                # 21 % 7 + (1 * 1) = 1 (taken)
                # 21 % 7 + (2 * 2) = 4 

hm.insert(5)    # h(5) = 5 % 7 + (0 * 0) = 5

hm.insert(8)    # h(8) = 8 % 7 + (0 * 0) = 1 (taken)
                # 8 % 7 + (1 * 1) = 2

hm.insert(19)   # h(19) = 19 % 7 + (0 * 0) = 5 (taken)
                # 19 % 7 + (1 * 1) = 6

hm.insert(28)   # h(28) = 28 % 7 + (0 * 0) = 0 (taken) Should be 3
                # 28 % 7 + (1 * 1) = 1 (taken)
                # 28 % 7 + (2 * 2) = 4 (taken) 
                # 28 % 7 + (3 * 3) = 9 (greater than M - 1 so we need to use modulo) 9 % 7 = 2 (taken)
                # 28 % 7 + (4 * 4) = 16 % 7 = 2 (taken) 
                # 28 % 7 + (5 * 5) = 25 % 7 = 4 (taken)
                # 28 % 7 + (6 * 6) = 36 % 7 = 1 (taken)
                # 28 % 7 + (7 * 7) = 49 % 7 = 7 % 7 = 0 (taken)
                # 28 % 7 + (8 * 8) = 64 % 7 = 1 (taken)
                # 28 % 7 + (9 * 9) = 81 % 7 = 4 (taken)
                # 28 % 7 + (10 * 10) = 100 % 7 = 2 (taken)
                # 28 % 7 + (11 * 11) = 121 % 7 = 2 (taken)
                # 28 % 7 + (12 * 12) = 144 % 7 = 4 (taken)
                # 28 % 7 + (13 * 13) = 169 % 7 = 1 (taken)
                # 28 % 7 + (14 * 14) = 196 % 7 = 0 (taken)
                # 28 % 7 + (15 * 15) = 225 % 7 = 1 (taken)
                # this is over our limit at this point

hm.insert(10)   # h(10) = 10 % 7 + (0 * 0) = 3
hm.insert(17)   # h(10) = 10 % 7 + (0 * 0) = 3

hm.list_print()

print('\n')

print(hm.search(10))

print('\n')

print(hm.remove(10))

print('\n')

hm.list_print()


