# default parametrs
def marks(m1=0, m2=0, m3=0, m4=0, m5=0):
    total = m1 + m2 + m3 + m4 + m5

    percentage = total / 5

    print(f"total: {total} and percentage: {percentage}")


marks(50, 30, 40, 50, 60)
marks(50, 30, 40, 50)
marks()


# required and optional parameters


def marks(
    m1, m2, m3=0, m4=0, m5=0
):  # required parameters always comes left side and optonal parameters comes right side.
    total = m1 + m2 + m3 + m4 + m5

    percentage = total / 5

    print(f"total: {total} and percentage: {percentage}")


marks(50, 30)


def intro(name, age=0, gender=""):
    print(name, age, gender)


intro("Prit")
