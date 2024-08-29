"""
Write a function that updates the values of a dictionary by multiplying
them by a given factor only if the value is an integer.
"""


def dict_mul(dct: dict, factor: int):
    new_dict = dct.copy()
    for k, v in new_dict.items():
        if isinstance(v, int):
            new_dict[k] = v * factor

    return new_dict


dct = {
    "a": 9,
    "b": "prit",
    "c": 7.5,
    "d": 10,
}

fact = 2
res = dict_mul(dct, fact)
print(res)
