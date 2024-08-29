# my_list: list = [5, 6, 7, 4]
# print(my_list)


# my_list.append(33, 44, 55) takes only one argumet
# print(my_list)

# my_list.append([33, 44, 55])
# print(my_list)

# my_list.extend([33, 44, 55])
# print(my_list)

# my_list.extend("Prit")  # since string is iterable object
# print(my_list)


# my_list: list = [5, 6, 7, 4, 4, 4, 4, 4]
# print(my_list.count(4))


# print(my_list.index(4))

my_list: list = [5, 10, 7, 4, 4, 4, 4, 4]
my_list.reverse()
print(my_list)

my_list: list = [5, 15, 7, 4, 4, 4, 4, 4]
my_list.sort()  # the id of the list will be same as sort method returns None, means sorting internally
print(my_list)

my_list.sort(reverse=True)
print(my_list)
