#
# DO NOT FORGET TO ADD COMMENTS
#

class Stack:
    
    def __init__(self):
        pass 

    def isEmpty(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass
    
    def peek(self):
        pass

    def size(self):
        pass

# a driver program for class Stack

if __name__ == '__main__':
    
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
