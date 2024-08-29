a, b, c = (1, 2, 3)  # unpacking
print(a, b, c)
print(type(a), type(b), type(c))

# it happens in list also.

x, y, z = [2, 3, "Prit"]
print(x, y, z)
print(type(x), type(y), type(z))

z = (56,)
print(z)
print(type(z))


# a, b, *c = (1, 2, 3, 4, 54, 6, 7, 78, 8, 10)
# print(f"a= {a}")
# print(f"b= {b}")
# print(f"c= {c}")

a, *b, c = (1, 2, 3, 4, 54, 6, 7, 78, 8, 10)
print(f"a= {a}")
print(f"b= {b}")
print(f"c= {c}")
