"""
Given a dictionary, write a function that returns a new dictionary
containing only the keys that have values of type str.
"""


def str_dict(my_dict: dict) -> dict:
    new_dict = {}
    for k, v in my_dict.items():
        if isinstance(v, str):
            new_dict[k] = v
    return new_dict


dct = {
    "a": 9,
    "b": "prit",
    "c": 7.5,
    "d": 10,
    "e": "pathak",
}

res = str_dict(dct)
print(res)
