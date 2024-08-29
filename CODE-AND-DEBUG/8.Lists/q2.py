"""
removing even numbers from the list
"""

# Method-1 : this method wil NEVER work, as it is changing the length of the list while iterating.
# NEVER CHANGE THE LENTGH OF THE LIST IN FOR LOOP-> POP METHOD WILL ELIMINATE  THE LIST'S ELEMENT AND CHANGES THE LENGTH
# my_list = [3, 4, 5, 6, 8, 67, 4, 2, 1]
# print(my_list)
# n = len(my_list)

# for i in range(n):
#     if my_list[i] % 2 == 0:
#         my_list.pop(i)

# print(my_list)

# Method 2 : use this approach always
my_list = [3, 4, 5, 6, 8, 67, 4, 2, 1]
print(my_list)
n = len(my_list)
res = []
for i in range(n):
    if my_list[i] % 2 != 0:
        res.append(my_list[i])


print(res)

# method3: use iterate by value
my_list = [3, 4, 5, 6, 8, 67, 4, 2, 1]

for item in my_list:
    if item % 2 == 0:
        my_list.remove(item)

print(my_list)
