# PARAMETERS AND ARGUMENTS


# def average(num1, num2, num3):  # PARAMETERS
#     average = (num1 + num2 + num3) / 3
#     print(average)


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# average(num1, num2, num3)  # Arguments


def avg(n1: int, n2: int, n3: int):
    total = n1 + n2 + n3

    print(f"total of 3 number : {total}")


avg(2, 3, 4)

avg("prit", "priyankar", "pathak")

# make a function marks, that takes 5 integers as a parameter and
# print total and percentage


def marks(m1: int, m2: int, m3: int, m4: int, m5: int):
    total = m1 + m2 + m3 + m4 + m5

    percentage = total / 5

    print(f"total: {total} and percentage: {percentage}")


marks(5, 3, 4, 5, 6)
