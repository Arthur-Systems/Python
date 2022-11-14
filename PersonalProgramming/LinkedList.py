class linkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert(head, data):
    if head == None:
        head = linkedList(data)
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = linkedList(data)
    return head


def printList(head):
    if head == None:
        return
    else:
        temp = head
        while temp != None:
            print(temp.data, "->", end=" ")
            temp = temp.next


def reverse(head):
    temp = None
    current = head
    while current:
        next = current.next
        current.next = temp
        temp = current
        current = next
    head = temp
    printList(head)


if __name__ == '__main__':
    PyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = None
    for i in PyList:
        head = insert(head, i)
    temp = head
    printList(head)
    temp = head
    reverse(head)
