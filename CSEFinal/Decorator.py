def verify(func):
    passcode = 'abc'

    def wrap(name, code):
        if code == passcode:
            func(name, code)
        else:
            print("Access denied!")
    return wrap


@verify
def login(name, code):
    print(f"Hello, {name}!")


name = input("Enter your name: ")
code = input("Enter the passcode: ")
login(name, code)
