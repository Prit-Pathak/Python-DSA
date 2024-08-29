"""
    1
   123
  12345
 1234567
123456789
"""


def pattern(n: int):
    for i in range(1, 6):
        for j in range(1, 5 - i + 1):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(k, end=" ")
        print()


n = 5
pattern(5)
