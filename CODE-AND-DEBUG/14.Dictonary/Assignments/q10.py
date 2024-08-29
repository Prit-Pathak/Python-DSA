"""
Write a Python program to combine two dictionary by adding values
for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
"""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

my_dict = {}

my_dict.update(d1)

for k, v in d2.items():
    if k in my_dict:
        my_dict[k] = my_dict[k] + v
    else:
        my_dict[k] = v

print(my_dict)
