# Recursion using Funcational way


def fibbo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibbo(num - 1) + fibbo(num - 2)


x = fibbo(4)
print(x)
