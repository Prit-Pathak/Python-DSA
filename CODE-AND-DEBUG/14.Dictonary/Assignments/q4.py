# function that takes a dictionary and a key, and returns True if
# the key is found in the dictionary, otherwise False


def ret_key(dct: dict, ky: str) -> bool:
    for k in dct:
        if k == ky:
            return True
    return False


dct = {"name": "Prit", "age": 56}
ky = "Prit"

res = ret_key(dct, ky)
print(res)
