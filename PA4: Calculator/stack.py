# author: Arthur Wei
# date: November 14, 2022
# file: stack.py a python file that creates a stack class
# input: Data to be inserted into the stack
# output:  Data that is popped from the stack

class Stack:  # a class that creates a stack
    def __init__(self, items=[]):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1] if not self.isEmpty() else None
    # returns the top of the stack without removing it but returns None if the stack is empty

    def size(self):
        return len(self.items)

# a driver program for class Stack


if __name__ == '__main__':

    # a list of data to be inserted into the stack
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
    print("All tests passed!")
