
class Heap:
    def __init__(self, data=None):
        self.data = data if data else []
        self.size = len(self.data)
        self.build(self.data)
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.data)

    def getParent(self, i):
        return (i-1) // 2 if i > 0 else None

    def getLeftChild(self, i):
        return i * 2 + 1

    def getRightChild(self, i):
        return i * 2 + 2

    def insert(self, data, item):
        data.append(item)
        self.size += 1
        self.build(data)

    def heapify(self, data, i):
        l = self.getLeftChild(i)
        r = self.getRightChild(i)
        smallest = i
        if l < self.size and data[l] < data[smallest]:
            smallest = l
        if r < self.size and data[r] < data[smallest]:
            smallest = r
        if smallest != i:
            data[i], data[smallest] = data[smallest], data[i]
            self.heapify(data, smallest)

    def build(self, data):
        self.size = len(data)
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(data, i)
        return data

    def MinExtract(self):
        Sorted = []
        while self.size > 0:
            Sorted.append(self.data[0])
            self.data[0] = self.data[self.size - 1]
            self.size -= 1
            self.heapify(self.data, 0)
        return Sorted


# You have a min-heap, write a function that takes a min-heap and returns a sorted list of the elements in the heap.
if __name__ == "__main__":
    Numbers = [5, 2, 3, 6, 9, 1, 7, 10, 14, 432, 53, 23, 12, 11, 8, 4]
    sortednum = Numbers.copy()
    sortednum.sort()
    print(f'Numbers: {Numbers}')
    print(f'Sorted Numbers: {sortednum}')
    heap = Heap(Numbers)
    print(f'Heaped: {heap}')
    print(sortednum)
    assert heap.MinExtract() == sortednum
    # heap.insert(Numbers, 0)
    # heap.insert(Numbers, 6)
    # heap.insert(Numbers, 43)
    # sortednum = Numbers
    # sortednum.sort()
    # print(sortednum)
    # print(heap)
    # assert heap.MinExtract() == sortednum
    # print("All tests passed")
