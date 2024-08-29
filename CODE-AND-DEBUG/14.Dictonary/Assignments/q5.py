"""
Given two dictionaries, write a function to merge them into a new
dictionary. If there is any overlap of keys, the value from the second
dictionary should overwrite the one from the first dictionary.
"""

dct1 = {"apple": 3, "banana": 5, "cherry": 7}
dct2 = {"banana": 8, "orange": 10, "apple": 9}

dct1.update(dct2)

print(dct1)
