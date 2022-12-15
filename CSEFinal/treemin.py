class Tree:
    def __init__(self, value='', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        s = str(self.value) + ':'
        if self != None:
            s += ' ' + str(self.left)
            s += ' ' + str(self.right)
        return s

# generate a tree from a list of items (data)


def build_tree(data, index):
    t = None
    if index < len(data):
        left = build_tree(data, index*2+1)
        right = build_tree(data, index*2+2)
        t = Tree(data[index], left, right)
    return t

# recursively traverse through all nodes in a tree and return the maximum value


def find_min(tree, minimum):
    # your code goes here
    if tree != None:
        if tree.value < minimum:
            minimum = tree.value
        minimum = find_min(tree.left, minimum)
        minimum = find_min(tree.right, minimum)
    return minimum


if __name__ == '__main__':
    data = [1, 2, 7, 4, 8, 6, 5]

    t = build_tree(data, 0)
    # find the minimum number, initially it is set to -inf
    m = find_min(t, float('inf'))
    print(m)
    assert m == min(data)
    print('Test passed')
