# general method
# my_lst = []

# for i in range(11):
#     my_lst.append(i)
# print(my_lst)

# list comprehension

my_lst = [i for i in range(11)]
print(my_lst)

my_lst1 = [i + 3 for i in range(11)]
print(my_lst1)

my_lst2 = [i for i in range(11, 0, -1)]
print(my_lst2)

my_lst3 = [-1 for i in range(0, 5)]
print(my_lst3)
my_lst3 = [-1 for _ in range(0, 5)]
print(my_lst3)
