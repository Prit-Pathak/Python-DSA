# def info():
#     pass

# print("egfub")


# scoping in function: local and global variable
def info():
    # local variables -> valiod only inside the function, we cannot acces them outside the function
    a = 200
    b = 800
    total = a + b
    print(total)


def greet():
    name = "Prit"
    print(f"hello {name}")


info()
greet()
greet()
