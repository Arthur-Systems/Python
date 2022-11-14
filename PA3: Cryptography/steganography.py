# author: Arthur Wei
# date: November 06, 2022
# file: steganography.py a Python program that encodes and decodes a message in an image
# input: None
# output: a message encoded in an image

#  type: ignore
# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher, HuffmanCodes


class Steganography():
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)

        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)

        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter=self.delimiter)
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter=self.delimiter)
        elif codec == 'huffman':
            self.codec = HuffmanCodes(delimiter=self.delimiter)
        binary = self.codec.encode(message + self.delimiter)

        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1
        if num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary
            # for each pixel in the image
            for data in np.nditer(image, op_flags=['readwrite']):
                if len(binary) > 0:
                    # if the first bit of the binary is 1 and the bit in the image is odd, add 1
                    if binary[0] == '1' and data % 2 != 0:
                        data[...] = data + 1
                    # if the first bit of the binary is 0 and the bit in the image is even, subtract 1
                    elif binary[0] == '0' and data % 2 == 0:
                        data[...] = data - 1
                else:
                    encoded_image = image  # save the encoded image
                    break  # break out of the loop
                binary = binary[1:]  # remove the first bit of the binary
            cv2.imwrite(fileout, encoded_image)  # save the encoded image

    def decode(self, filein, codec):
        flag = True
        image = cv2.imread(filein)
        if codec == 'binary':
            self.codec = Codec(delimiter=self.delimiter)
        elif codec == 'caesar':
            self.codec = CaesarCypher(delimiter=self.delimiter)
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            binary_data = ''
            for data in np.nditer(image):
                binary_data += '1' if data % 2 == 0 else '0'

            self.text = self.codec.decode(binary_data)
            self.binary = self.codec.encode(
                self.text + self.delimiter)

    def print(self):  # print the message
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()
