

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_palindrome(s):
    word = Stack()
    rword = Stack()
    storage = Stack()
    for char in s:
        word.push(char)
        storage.push(char)
    while not word.isEmpty():
        rword.push(word.pop())
    while not storage.isEmpty():
        if storage.pop() != rword.pop():
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))
    print(is_palindrome("boo"))
    print(is_palindrome("kkokk"))
    print(is_palindrome("treat"))
