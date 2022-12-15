def foo():
    n = 0
    while True:
        n += 1
        yield n


for i in range(10):
    f = foo()
    print(next(f))
