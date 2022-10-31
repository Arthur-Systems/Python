# print numbers iteratively
from timeit import Timer, timeit
from functools import lru_cache


def print_numbers(n):
    for i in range(1, n+1):
        print(i)


# main program
print_numbers(10)

# print numbers recursively


def print_numbers(n):
    if n == 1:           # the base case
        print(n)
    else:
        print_numbers(n-1)  # recursive call
        print(n)


# main program
print_numbers(10)

# using a generator


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    for i in all_perms(data):
        print(i)

# Function to create combinations


def all_combs(list_, n):
    if n == 0:
        return [[]]
    l = []
    for i in range(0, len(list_)):
        m = list_[i]
        r = list_[i+1:]

        for p in all_combs(r, n-1):
            l.append([m] + p)
    return l


# Driver code
if __name__ == "__main__":
    items = "abcd"
    print(all_combs([x for x in items], 3))


# naive implementation of the Fibonacci function


def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

# using a cache for the Fibonacci function


def fib2(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        cache[n] = n
        return n
    else:
        cache[n] = fib2(n-1) + fib2(n-2)
        return cache[n]


@lru_cache()
# using the caching system in Python for the Fibonacci function
def fib3(n):
    if n <= 1:
        return n
    else:
        return fib3(n-1) + fib3(n-2)


# calls Fibonacci function
print(fib1(4))
cache = {}
print(fib2(4))
print(fib3(4))

print(type(cache))

t1 = Timer("fib1(15)", "from __main__ import fib1")
print("fib1 ", t1.timeit(number=1), "milliseconds")
t2 = Timer("fib2(15)", "from __main__ import fib2")
print("fib2 ", t2.timeit(number=1), "milliseconds")
t3 = Timer("fib3(15)", "from __main__ import fib3")
print("fib3 ", t3.timeit(number=1), "milliseconds")
