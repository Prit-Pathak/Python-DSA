my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]

"""
{
   4: 4, 5: 1, 6: 1, 3: 3, 2: 1, 10: 2, 8: 1, 9: 2,
}
"""
my_dict = {}

for num in my_list:
    if num in my_dict:
        my_dict[num] = my_dict[num] + 1
    else:
        my_dict[num] = 1

print(my_dict)
