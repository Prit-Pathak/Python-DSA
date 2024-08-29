"""
    5
   444
  33333
 2222222
111111111
"""


def pattern(n: int):
    for i in range(1, 6):
        for j in range(1, 5 - i + 1):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(n - i + 1, end=" ")
        print()


n = 5
pattern(5)
