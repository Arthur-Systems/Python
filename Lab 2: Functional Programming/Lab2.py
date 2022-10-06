# Note the pattern: (lambda parameters : expression) (*argv)
from functools import reduce
result = (lambda x, y: x + y)(2, 3)
print(result)

# save a lambda fxn into a variable!!!
# notice that we do not use the function definition!


def sum(x, y): return x + y


result = sum(4, 3)
print(result)

# returns True or False depending on the number


def is_even(x): return True if x % 2 == 0 else False


result = is_even(4)
print(result)

# return a map object (an iterator) that can be converted into a list
# define input
nums = [3, 24, 5, 8]

# apply map


def cube(x): return x**3


cube_map = map(cube, nums)
print(cube_map)

# convert map into list
print(list(cube_map))

nums2 = [3, 2, 1]
cube_list = list(map(lambda x: x**3, nums2))
print(cube_list)

# return a Filter object (an iterator) that can be converted into a list
# define input
nums = [3, 24, 5, 8]

# apply filter


def is_even(x): return True if x % 2 == 0 else False


even_filter = filter(is_even, nums)

# convert filter into list
even_list = list(even_filter)
print(even_list)

# or we can combine the filter code in one line
nums2 = [3, 2, 1]
even_list = list(filter(lambda x: True if x % 2 == 0 else False, nums2))
print(even_list)

# iterate two items at a time and return a single result (sum, product, etc.)

# define input
nums = [3, 24, 5, 8]

# find sum
sum_ = reduce(lambda x, y: x + y, nums)
print(sum_)

# find product
product = reduce(lambda x, y: x * y, nums)
print(product)


def decorator(func):
    def wrap():
        print("======")
        func()
        print("======")
    return wrap


@decorator
def printName():
    print("John!")


if __name__ == ‘__main__’:
    printName()
