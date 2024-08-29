my_lst = [33, 44, 55, 667, 8, 9, 3, 11]
print(f"my list is : {my_lst}")
print(f"my list id is : {id(my_lst)}")

my_lst[:] = [1, 3, 4]
print(f"my list is : {my_lst}")
print(f"my list id is : {id(my_lst)}")


b = my_lst
print(f"my list is : {b}")
print(f"my list id is : {id(b)}")

c = my_lst[:]  # similar to .copy(), means id will be change
print(f"my list is : {c}")
print(f"my list id is : {id(c)}")

my_lst[:] = my_lst[:4]  # this will chnage the original list itself
print(my_lst)
