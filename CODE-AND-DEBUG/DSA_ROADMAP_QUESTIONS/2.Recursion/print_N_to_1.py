"""
Print numbers from 1 to N
"""


# Without backtracking
def func(i, n):
    if i < 1:
        return
    print(i)
    func(i - 1, n)


# With backtracking
def func2(i, n):
    if i > n:
        return
    func2(i + 1, n)
    print(i)


if __name__ == "__main__":
    n = 5
    func(5, 1)
    print()
    func2(1, 6)
