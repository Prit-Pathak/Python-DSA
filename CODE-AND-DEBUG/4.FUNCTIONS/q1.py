"""
Make a function which as 5 integer parameters as a subject
Return True if pass
else False
"""


def ifpass(m1: int, m2: int, m3: int, m4: int, m5: int) -> bool:
    total = m1 + m2 + m3 + m4 + m5
    per = total / 5

    # if per > 60:
    #     return True
    # else:
    #     return False
    return per >= 60


a = ifpass(33, 55, 67, 89, 90)
print(a)
