from decimal import *
from fractions import Fraction
num1, num2, num3, num4 = 125, 21, 30, 16

# complex numbers
cnum1 = complex(num1, num2)
cnum2 = complex(num2, num4)
print(cnum1, cnum2)
# conj(x1+y1*i)  = x1-y1*i
print(cnum1.conjugate())
# (x1+y1*i) + (x2+y2*i)  = (x1+x2)+(y1+y2)*i
print(cnum1 + cnum2)
# (x1+y1*i)*(x2+y2*i) = (x1*x2-y1*y2)+(x1*y2+y1*x2)*i
print(cnum1 * cnum2)
# (x1+y1*i)/(x2+y2*i) = [(x1*x2+y1*y2)+(y1*x2-x1*y2)*i] /(x2*x2+y2*y2)
print(cnum1 / cnum2)


num1, num2, num3, num4 = 125, 21, 30, 16

# fractions
frac1 = Fraction(num1, num2)
print(frac1)

frac2 = Fraction(num3, num4)
print(frac2)

print(frac1 + frac2)

print(frac1 * frac2)

print(frac1 / frac2)


num1, num2, num3, num4 = 125, 21, 30, 16

# decimal numbers
print(num1/num2)

getcontext().prec = 13   # set the decimal precision
dec1 = Decimal(num1)/Decimal(num2)
print(dec1)

getcontext().prec = 3   # note the precision!!!
print(dec1)

dec2 = Decimal(num3)/Decimal(num4)
print(dec2)


# binary, octal , hexadecimal
num1_binary = bin(125)
print(num1_binary)

print(type(num1_binary))

num1_octal = oct(125)
print(num1_octal)
print(type(num1_octal))

num1_hex = hex(125)
print(num1_hex)

print(type(num1_hex))

num1 = 125
print(num1.bit_length())

print(int(num1_binary, 2))

print(int(num1_hex, 16))

# make bytes
print(bytes(5))  # make 5 bytes equals to 0

print(bytes([97, 98, 99]))  # make 3 bytes equals to 97, 98, 99

print(b'abc')

print('abc'.encode('utf-8'))  # using string, method 2

print(bytes('abc', 'utf-8'))  # using string, method 3

print('abc'.encode('utf-16'))

print('abc'.encode('utf-16-le'))

# # bytes are not mutable
# a = bytes('abc', 'utf-8')
# a[1] = 102  # bytes are immutable!!! Write the error message, last line

# bytearray
print(bytearray(5))

print(bytearray([1, 2, 3]))

print(bytearray('abc', 'utf-8'))

print(bytearray('abc', 'utf-16'))

# bytearray is mutable
b = bytearray('abc', 'utf-8')
print(b)

b[1] = 114
print(b)

# convert into strings
a = bytes('abc', 'utf-8')
print(a)
print(a.decode('utf-8'))

b = bytearray('abc', 'utf-16-le')
print(b)
bytearray(b'a\x00b\x00c\x00')
print(b.decode('utf-16-le'))

# concatenate bytes and bytearray
print(a+b)  # write the answer for the last print statement


# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # prints the formal object's information
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)

    # prints the readable form, used by print()
    def __str__(self):
        return '%s + %si' % (self.real, self.imag)


# Driver program to test the class
if __name__ == '__main__':
    t = Complex(10, 20)
    print(type(t))
print(t)
print(str(t))
print(repr(t))
