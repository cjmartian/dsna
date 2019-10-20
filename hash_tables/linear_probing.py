class Node:
    data = None

    def __init__(self, data):
        self.data = data

class HashMap:
    del_symbol = -1  # assumes that we will only have posivite int in our hash
    
    def __init__(self, init_size):
        self.init_size = init_size
        self.store = [None for _ in range(init_size)]
        self.size = 0

    def _hash(self, key, n):
        # need to check that n < self.init_size - 1
        if isinstance(key, int):
            start = key % self.init_size
            index = start + n
            if index > (self.init_size - 1):
                index = index - (self.init_size - 1)
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
        while start < self.init_size:
            index = self._hash(v, start)
            if not self.store[index]:
                return '{} is not in the hash'.format(v)
            curr = self.store[index]
            if v == curr.data:
                return index
            start  += 1
        return '{} is not in the hash.'.format(v)

    def insert(self, v):
        new_node = Node(v)
        start = 0
        while start < self.init_size:
            index = self._hash(v, start)
            if not self.store[index] or self.store[index] == self.del_symbol:
                self.store[index] = new_node
                return index
            start += 1
        return 'No more space in the hash!'
    
    def remove(self, v):
        start = 0
        while start < self.init_size:
            index = self._hash(v, start)
            if not self.store[index]:
                return '{} is not in the hash'.format(v)
            curr = self.store[index]
            if v == curr.data:
                self.store[index] = self.del_symbol
                return index
            start  += 1
        return '{} is not in the hash.'.format(v)



hm = HashMap(7)

hm.insert(7)
hm.insert(8)
hm.insert(12)
hm.insert(14)

print(hm.search(14))
print(hm.search(32))
print(hm.search(12))

print('\n')

hm.list_print()

print('\n')

hm.remove(8)

hm.list_print()

print('\n')

hm.insert(22)
hm.insert(15)
hm.insert(150)
hm.insert(151)
hm.insert(152)
hm.insert(153)

hm.list_print()
