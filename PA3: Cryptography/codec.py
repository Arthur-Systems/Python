# author: Arthur Wei
# date: November 06, 2022
# file: codec.py a Python program that encodes and decodes a message in an image
# input: the image file
# output: a message encoded in an image
import numpy as np
from collections import Counter


class Codec():
    # constructor
    def __init__(self, delimiter='#'):
        self.name = 'binary'
        self.delimiter = delimiter

    # convert text or numbers into binary form
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []
        for i in range(0, len(data), 8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte, 2))
        return text


class CaesarCypher(Codec):
    # constructor
    def __init__(self, delimiter="#", shift=3):
        self.name = 'caesar'
        self.delimiter = delimiter
        self.shift = shift
        self.chars = 256      # total number of characters

    # convert text or numbers into binary form
    def encode(self, text):
        data = ''
        if type(text) == str:
            # shift the character by 3
            return ''.join([format((ord(i) + self.shift) % 256, "08b") for i in text])
        else:
            print('Format error')
        return data

    # convert binary data into text
    def decode(self, data):
        text = ''
        if type(data) == str:
            for i in range(0, len(data), 8):
                byte = data[i: i+8]
                if byte == self.encode(self.delimiter):
                    break
                # shift the character back 3
                text += chr(int(byte, 2) - self.shift)

        return text

# a helper class used for class HuffmanCodes that implements a Huffman tree


class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''


class HuffmanCodes(Codec):

    def __init__(self, delimiter='#'):
        self.nodes = None
        self.data = {}
        self.name = 'huffman'
        self.delimiter = delimiter

    # make a Huffman Tree
    def make_tree(self, data):
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
            left.code = '0'
            right.code = '1'

            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)

            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        self.nodes = nodes
        return nodes

    # traverse a Huffman tree
    def traverse_tree(self, node, val):
        next_val = val + node.code
        if (node.left):
            self.traverse_tree(node.left, next_val)
        if (node.right):
            self.traverse_tree(node.right, next_val)
        if (not node.left and not node.right):
            self.data[node.symbol] = next_val

    # convert text into binary form
    def encode(self, text):
        data = ''
        self.make_tree(Counter(text))  # make a Huffman tree
        data = self.traverse_tree(self.nodes[0], '')  # traverse the tree
        return ''.join([self.data[i] for i in text])  # return the binary data

    # convert binary data into text
    def decode(self, data):
        text = ''
        temp = ''
        for bit in data:  # for each bit in the binary data
            temp += bit  # add the bit to the temporary string
            for char, binary in self.data.items():  # for each character and its binary code in the dictionary
                # if the temporary string is the delimiter
                if temp == self.data[self.delimiter]:
                    break  # break out of the loop
                elif temp == binary:               # if the temporary string is in the dictionary
                    text += char                   # add the character to the text
                    temp = ''                     # reset the temporary string
                else:
                    continue                     # otherwise, continue to the next character
        return text  # return the text


# driver program for codec classes
if __name__ == '__main__':
    text = 'hello'
    print('Original:', text)

    c = Codec()
    binary = c.encode(text + c.delimiter)
    print('Binary:', binary)
    data = c.decode(binary)
    print('Text:', data)

    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    print('Binary:', binary)
    data = cc.decode(binary)
    print('Text:', data)

    h = HuffmanCodes()
    binary = h.encode(text + h.delimiter)
    print('Binary:', binary)
    data = h.decode(binary)
    print('Text:', data)
