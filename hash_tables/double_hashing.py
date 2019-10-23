class Node:
    def __init__(self, data):
        self.data = data

class HashTable:
    del_symbol = -1

    def __init__(self, init_size, second_prime):
        self.init_size = init_size
        self.second_prime = second_prime
        self.size = 0
        self.store = [None for _ in range(self.init_size)]
        self.limit = 15

    def _hash(self, v, n):
        
        def hash_one(v):
            return v % self.init_size

        def hash_two(v):
            return (self.second_prime - (v % self.second_prime))
        if n == 0:
            return hash_one(v=v)
        else:
            return (hash_one(v=v) + (n * hash_two(v=v))) % self.init_size
                
    def list_print(self):
        for i in self.store:
            if i and i is not self.del_symbol:
                print(i.data)
            else:
                print(i)
        
    def search(self, v):
        count = 0
        while count <= self.limit:
            index = self._hash(v, count)
            node = self.store[index] 
            if not node or node is self.del_symbol:
                continue
            elif node.data == v:
                return index
            count += 1

    def insert(self, v):
        if self.size >= self.init_size:
            return 'Table is full, cannot insert {}'.format(v)
        count = 0
        new_node = Node(v)
        while count <= self.limit:
            index = self._hash(v, count)
            if not self.store[index] or self.store[index] is self.del_symbol:
                self.store[index] = new_node
                self.size += 1
                return index
            count += 1
        return "Could not find a spot for {}".format(v)

    def remove(self, v):
        count = 0
        while count <= self.limit:
            index = self._hash(v, count)
            node = self.store[index]
            if not node or node is self.del_symbol:
                print('not here! {}'.format(count))
                continue
            elif node.data == v:
                self.store[index] = self.del_symbol
                self.size -= 1
                return index
            count += 1


ht = HashTable(7, 5)
ht.insert(14)
ht.insert(17)
ht.insert(12)
ht.insert(35)
ht.insert(42)
ht.insert(98)
ht.insert(79)

ht.list_print()

print('\n')

print(ht.search(17))

print('\n')

ht.remove(17)

ht.list_print()
