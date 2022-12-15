from stack import Stack


class PQueue:
    def __init__(self):
        self.stack = Stack()

    def __str__(self):
        return str(self.stack)

    def empty(self):
        return self.stack.isEmpty()

    def enqueue(self, item):
        if self.empty():
            self.stack.push(item)
        else:
            temp = Stack()
            while not self.empty():
                if item < self.stack.peek():
                    temp.push(self.stack.pop())
                else:
                    break
            self.stack.push(item)
            while not temp.isEmpty():
                self.stack.push(temp.pop())

    def dequeue(self):
        return self.stack.pop()


if __name__ == '__main__':
    pq = PQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        pq.enqueue(i)
        print('adding', i)
        print(pq)

    while not pq.empty():
        print('removing', pq.dequeue())
        print(pq)
