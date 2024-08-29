"""
Keep asking a number from user until he enters zero (0)
Calculate total
"""


def ask_total():
    sum = 0
    while True:
        n = int(input())
        if n == 0:
            break
        sum += n
    return sum


a = ask_total()
print(a)
