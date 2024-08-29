lst = [4, 5, 6, 5, 4, 4, 7]
my_dict = {}
max_freq_num = 0
for item in lst:
    my_dict[item] = my_dict.get(item, 0) + 1
    if my_dict[item] > max_freq_num:
        max_freq_num = my_dict[item]

print(my_dict)
print(max_freq_num)
