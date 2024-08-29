my_list = [52, 74, 89, 4, 8, 74, 5, 4, 233, 4]
print(my_list)
my_list.insert(1, "Prit")
print(my_list)

my_list.insert(50, 111)
print(my_list)

my_list.insert(-2, True)
print(my_list)


x = my_list.pop()
print(x)
print(my_list)

x = my_list.pop(1)  # del by index
print(x)
print(my_list)


del my_list[0]
print(my_list)

my_list.remove(
    4
)  # del by value, if same val occurs multiple times, deletes the firstr occurance of the value
print(my_list)

my_list.clear()  # clear all the lements of the list but not the lists
print(my_list)
