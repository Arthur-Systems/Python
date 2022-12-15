

if __name__ == '__main__':

    def foo(n):
        return [x*x for x in range(n)]

    def x(x): return [x*x for x in range(x)]
    print(x(10))
