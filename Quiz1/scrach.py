def recursive(n):
    if n == 1:
        return 1
    else:
        return n * recursive(n - 1)


class Fraction:
    def __init__(self, top, bottom):
        if type(top) == type(bottom) == int:
            # gcd finds the greatest common divisor of two numbers
            # common = gcd(top, bottom)
