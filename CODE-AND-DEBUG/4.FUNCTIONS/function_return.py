def add(n1, n2):
    total = n1 + n2
    return total  # this function return total value


def add_without_return(n1, n2):
    total = n1 + n2
    print(total)  # this fxn does not return anything, simply printing the value


def even(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


x = add(5, 6)

y = even(x)
print(y)
