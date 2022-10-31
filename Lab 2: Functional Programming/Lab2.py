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


if __name__ == '__main__':
    printName()

# create a decorator that takes in parameters


def run_times(num):
    def wrap(func):
        for i in range(num):
            func()
    return wrap


@run_times(4)
def sayHello():
    print("Hello!", end=" ")

# create a decorator for a function that accepts parameters


def birthday(func):
    def wrap(name, age):
        func(name, age + 1)
    return wrap


@birthday
def celebrate(name, age):
    print("Happy birthday {}, you are now {}.".format(name, age))


celebrate("Paul", 43)

# restrict function access


# def login_required(func):
#     def wrap(user):
#         password = input("What is the password?")
#         if password == user["password"]:
#             func(user)
#         else:
#             print("Access Denied")
#     return wrap


# @login_required
# def restrictedFunc(user):
#     print("Access granted, welcome {}!".format(user["name"]))


# user = {"name": "Jess", "password": "ilywpf"}
# restrictedFunc(user)

word = "abc"
iter_ = iter(word)
print(type(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))
# print(next(iter_))


def generator1():
    s = "The first string"
    yield s
    s = "The second string"
    yield s


g1 = generator1()
print(type(g1))
print(next(g1))
print(next(g1))
g1 = generator1()
for k in g1:
    print(k)


def generator2():
    n = 0
    while True:
        yield n
        n += 1


g2 = generator2()
i = 0
while i < 3:
    print(next(g2), end=" ")
    i += 1
# x = [0, 1, 2, …, 999], x is a list of 1000 numbers
x = list(range(1000))
for k in x:
    print(k)
print(type(x))

y = range(1000)
for k in y:
    print(k)
print(type(y))


def my_range(stop, start=0, step=1):
    n = start
    print(start, stop, step)
    while (n < stop and step > 0) or (n > stop and step < 0):
        yield n
        n += step

    # for k in my_range(10):
    #     print(k, end=" ")

    # note that the order of arguments (stop, start, step) is different
# from the built-in function range order (start, stop, step)!!!
# for k in my_range(0, 10, -1):
#     print(k, end=" ")


# nums = [x for x in range(10)]
# print(nums)

# squares = [x**2 for x in range(1, 11)]
# print(squares)

# odd_nums = [x for x in range(10) if x % 2 == 1]
# print(odd_nums)

filter_nums = [0 if x % 2 == 0 else 1 for x in range(10)]
print(filter_nums)

nums = [x for x in range(10)]
cubes = {n: n**3 for n in nums}
print(cubes)

words = ['parent', 'mom', 'dad', 'daughter', 'son']
d = {n: len(n) for n in words}
print(d)

nums = [x for x in range(10)]
set1 = {var for var in nums if var % 2 == 0}
print(sorted(set1))

words = ['parent', 'mom', 'dad', 'daughter', 'son']
set2 = {n[::-1] for n in words}
print(sorted(set2))

nums = [x for x in range(10)]
gen = (x for x in nums if x % 2 == 0)
print(type(gen))

print("Generator sequence:", end=' ')
for k in gen:
    print(k, end=' ')

words = ['parent', 'mom', 'dad', 'daughter', 'son']
palindrome_selector = (x for x in words if x == x[::-1])
print("\nPalindromes:", end=' ')
for k in palindrome_selector:
    print(k, end=' ')
