# Recursion using Funcational way


def pow(base, power):
    if power == 0:
        return 1
    if power == 1:
        return base
    return base * pow(base, power - 1)


x = pow(4, 0)
print(x)
