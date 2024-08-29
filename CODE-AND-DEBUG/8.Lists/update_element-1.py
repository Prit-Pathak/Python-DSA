my_lst = [4, 5, 6, 7, 8, 9, 100]

n = len(my_lst)

# for i in range(0, n):
#     if my_lst[i] % 2 == 0:
#         my_lst[i] += 5


for i in range(0, n):
    if my_lst[i] % 2 == 0:
        my_lst[i] += 2
    else:
        my_lst[i] -= 2
print(my_lst)
