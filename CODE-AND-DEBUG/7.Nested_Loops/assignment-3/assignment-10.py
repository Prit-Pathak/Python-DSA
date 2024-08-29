"""
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
"""


def pattern(n: int):
    for i in range(1, (n // 2) + 2):
        for j in range(1, 5 - i + 1):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(k, end=" ")
        print()

    for i in range(n // 2, 0, -1):
        for j in range(1, (n // 2) - i + 2):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(k, end=" ")
        print()


n = 9
pattern(n)
