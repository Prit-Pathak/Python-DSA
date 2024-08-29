"""
i-> 1 - 10
1,3,5,7,9 = ODD
2,4,6,8,10 = EVEN
"""

my_list = ["even" if i % 2 == 0 else "odd" for i in range(11)]
print(my_list)
