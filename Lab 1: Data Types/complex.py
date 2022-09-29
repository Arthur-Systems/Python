# A user defined class to represent Complex numbers
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Complex(%s, %s)' % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        if self.imag < 0:
            return '%s - %si' % (self.real, self.imag*(-1))
        else:
            return '%s + %si' % (self.real, self.imag)

    # use the equation: (x1+y1*i) + (x2+y2*i)  = (x1+x2)+(y1+y2)*i
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __add__(self, other):
        if type(other) == type(self):
            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

    # use the equation: (x1+y1*i) - (x2+y2*i)  = (x1-x2)+(y1-y2)*i
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __sub__(self, other):
        if type(other) == type(self):
            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

    # use the equation:(x1+y1*i)*(x2+y2*i) = (x1*x2-y1*y2)+(x1*y2+y1*x2)*i
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __mul__(self, other):
        if type(other) == type(self):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

    # use the equation:(x1+y1*i)/(x2+y2*i) = [(x1*x2+y1*y2)+(y1*x2-x1*y2)*i] /(x2*x2+y2*y2)
    # where x1, x2 are real parts and y1, y2 are imaginary parts of two numbers
    def __truediv__(self, other):
        if type(other) == type(self):
            real = (self.real * other.real + self.imag * other.imag) / \
                (other.real * other.real + other.imag * other.imag)
            imag = (self.imag * other.real - self.real * other.imag) / \
                (other.real * other.real + other.imag * other.imag)
            return Complex(real, imag)
        else:
            raise TypeError('TypeError: unsupported operand type')

    def __eq__(self, other):
        if type(other) == type(self):
            return self.real == other.real and self.imag == other.imag
        else:
            raise TypeError('TypeError: unsupported operand type')


# Driver program to test the class
if __name__ == '__main__':
    t1 = Complex(1, 2)
    t2 = Complex(2, 3)
    print(t1 + t2)
    print(t2 - t1)
    print(t1 * t2)
    print(t1 / t2)
    print(t1 == t2)
    t3 = Complex(1, 1)
    print(t3 == (t2 - t1))
