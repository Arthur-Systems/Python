# A Huffman tree node
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


class HTree:
    def __init__(self, data):
        self.nodes = self.make_htree(data)

    def make_htree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))

        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)

            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]

            # assign codes
            left.code = 0
            right.code = 1

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        return nodes

    # print Huffman codes
    def print_codes(self, node=None, val=''):
        if node == None:
            node = self.nodes[0]
        newVal = val + str(node.code)
        if (node.left):
            self.print_codes(node.left, newVal)
        if (node.right):
            self.print_codes(node.right, newVal)
        if (not node.left and not node.right):
            print(f"{node.symbol} -> {newVal}")


if __name__ == '__main__':
    text = 'this is an example of a huffman tree'
    data = {}
    for i in text:
        data[i] = data.get(i, 0)+1
    print(data)
    htree = HTree(data)
    htree.print_codes()
