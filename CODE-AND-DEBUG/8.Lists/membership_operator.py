# membership operator -> in / not in -> returns Ture / False

# my_list = [3, 5, 6, 7, 4, 66, 7]

# print(6 in my_list)
# print(10 in my_list)

# use case

my_list = [2, 43, 5, 6, 7, 8, 5, 5, 5, 5, 6, 6, 7, 6, 3, 2, 3, 4, 65, 677]

res = []

for item in my_list:
    if item not in res:
        res.append(item)

print(res)
