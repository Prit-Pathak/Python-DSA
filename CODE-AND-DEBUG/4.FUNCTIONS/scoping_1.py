def info():
    # local variables
    a = 200
    b = 800
    total = a + b
    print(total)
    greet()


def greet():
    name = "Prit"
    print(f"hello {name}")
    info()


info()

# we can use it, but it will go in infifnite loop.
