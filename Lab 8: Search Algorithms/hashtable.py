class Hashtable:
    def __init__(self):
        self.size = 8
        self.table = [[], [], [], [], []]

    def hash(self, astring, size):
        sum = 0
        for pos in range(len(astring)):
            sum = sum + ord(astring[pos])
        return sum % size

    def add(self, key, value):
        index = self.hash(key, self.size)
        while index >= len(self.table):
            self.table.append([])
        self.table[index].append((key, value))

    def remove(self, key):
        index = self.hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return True
        return False

    def get(self, key):
        index = self.hash(key, self.size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def get_size(self):
        return self.size

    def is_empty(self):
        for item in self.table:
            if not item or len(item) == 0:
                continue
            return False
        return True


if __name__ == "__main__":
    data = ['goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', 'cow', 'cat']

    # make a hash table with key-value pairs: 'goat': 0, 'pig': 1, 'chicken': 2, etc.
    h = Hashtable()
    for i in range(len(data)):
        h.add(data[i], i)       # the key is data[i], the value is i

    # print the hash table items
    for key in data:
        print(h.get(key))

    # test the method get() and if items in the hash table are correct
    for i in range(len(data)):
        assert h.get(data[i]) == i

    # test the method get_size()
    n = h.get_size()
    assert n == 8

    # test the method remove() and is_empty()
    for i in data:
        h.remove(i)
    print(h.is_empty())
    assert h.is_empty()
