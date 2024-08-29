my_lst = [4, 5, 7, 89, 54, 3, 2, 56, 6, 7]
print(my_lst.sort())  # inplace sorting
# print(my_lst)

# my_list = [4, 5, 3, 2, 7, 8, 6, 8, 9, 3]
# print(my_list)
# print(id(my_list))

# my_list.sort()  # In place sorting
# print(my_list)
# print(id(my_list))

# print(sorted(my_list))
# print(my_list)


my_list = [4, 5, 3, 2, 7, 8, 6, 8, 9, 3]

# print("-".join(str(num) for num in my_list.sort()))
print("-".join(str(num) for num in sorted(my_list)))

print(my_list)


print(sorted("Huyh$^#&bkkh"))
