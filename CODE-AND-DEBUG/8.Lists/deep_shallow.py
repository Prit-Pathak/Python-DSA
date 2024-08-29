# a = [2, 3, 4, 5, 6, 7, 83, 56]

# b = a

# print(f"id pf a = {id(a)}")
# print(f"id pf b = {id(b)}")

# print(f"a = {a}")
# print(f"b = {b}")

# b[0] = 6565

# print(f"a = {a}")
# print(f"b = {b}")

# to overcome this we use shallow copy

# a = [2, 3, 4, 5, 6, 7, 83, 56]

# b = a.copy()

# print(f"id pf a = {id(a)}")
# print(f"id pf b = {id(b)}")

# now the address of both list is different, so if we change the fist list,
# the second list will not be changed

# another example of shallow  copy

a = [2, 3, 4, [100, 200, 300], 83, 56]

b = a.copy()

print(f"id pf a = {id(a)}")
print(f"id pf b = {id(b)}")

print(f"a = {a}")
print(f"b = {b}")

b[3][0] = 555  # here, this chane will occur in both the list, as shallow copy
# will not copy the ineer mutable object.

print(f"a = {a}")
print(f"b = {b}")

b[1] = 111  # this change will occur in one list, as this is outer list
print(f"a = {a}")
print(f"b = {b}")

#  now to over this scenario, we use deep copy

from copy import deepcopy

a = [2, 3, 4, [100, 200, 300], 83, 56]

b = deepcopy(a)

print(f"id pf a = {id(a)}")
print(f"id pf b = {id(b)}")

print(f"a = {a}")
print(f"b = {b}")

b[3][0] = 555

print(f"a = {a}")
print(f"b = {b}")
