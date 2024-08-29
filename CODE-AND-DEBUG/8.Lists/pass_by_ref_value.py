# pass by reference


def printing_list(lst: list) -> None:
    lst[0] = 100


my_list = [4, 5, 6, 7, 8, 9, 100]
print(my_list)
printing_list(my_list)
print(my_list)
