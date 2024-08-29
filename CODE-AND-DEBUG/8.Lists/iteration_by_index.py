my_lst = [22, 44, 55, 667, 89, 456, 555, 123]

n = len(my_lst)
print(n)

# Iterate by Index
for i in range(0, n):
    print(my_lst[i], end=" ")
print()
# reverse
for j in range(n - 1, -1, -1):
    print(my_lst[j], end=" ")
