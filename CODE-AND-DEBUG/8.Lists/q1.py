"""
ask a number from user = 6
take input number 6 times and at last print all elements in the list

enter num: 4
enter num: 56
enter num: 47
enter num: 66
enter num: 434
enter num: 55

o/p : [4,56,47,66,434,55]
"""

# n = int(input("enter len: "))
# lst = []
# for i in range(n):
#     num = int(input())
#     lst.append(num)

# print("list is: ", lst)

# method 2

from typing import List


def print_lst(len: int) -> List[int]:
    lst = []
    for i in range(len):
        num = int(input())
        lst.append(num)
    return lst


lst = print_lst(6)
print(lst)
