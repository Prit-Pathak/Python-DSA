"""
 Given a dictionary with key-value pairs, remove all the keys with
values greater than K, including mixed values.
Input : test_dict = {"Gfg" : 3,
‘is’ : 7,
‘best’ : 10,
‘for’ : 6,
‘xyzx’ : ‘CS’}, K = 7

Output : {‘Gfg’ : 3,
‘for’ : 6,
‘xyzx’ : ‘CS’}
Explanation : All values greater than K are removed. Mixed value is
retained.

Input : test_dict = {‘Gfg’ : 3,
‘is’ : 7,
‘best’ : 10,
‘for’ : 6,
‘qqqq’ : ‘CS’}, K = 1
Output : {‘qqqq’ : ‘CS’}
Explanation : Only Mixed value is retained
"""


def rem_ele_dict(my_dict: dict, k: int) -> dict:
    res = {}
    for key, value in my_dict.items():
        if isinstance(value, int) or isinstance(value, int):
            if value >= k:
                continue
            else:
                res[key] = value
        else:
            res[key] = value

    return res


my_dict = {
    "Gfg": 3,
    "is": 7,
    "best": 10,
    "for": 6,
    "xyzx": "CS",
}

k = 7

z = rem_ele_dict(my_dict, k)
print(z)
