
def bisect(f, a, b):
    for i in f:

    print(f)
    print(f(a), f(b))
    if f(a) * f(b) >= 0:
        print("You have not assumed right a and b")
        return None
    c = (a + b) / 2
    while (b - a) >= 0.01:
        # Check if middle point is root
        if f(c) == 0.0:
            break
        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c


if __name__ == "__main__":
    coefficients = input("Enter the polynomial coefficients:")
    coefficients = coefficients.split()
    coefficients = [float(i) for i in coefficients]
    print(coefficients)
    interval = input("Enter the interval:")
    interval = interval.split()
    interval = [int(i) for i in interval]
    print(bisect(, interval[0], interval[1]))
