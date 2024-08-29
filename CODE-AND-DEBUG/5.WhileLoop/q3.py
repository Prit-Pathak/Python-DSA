"""
ask a start num from user ->6
ask a end num from user ->15
print -> 6,7,8,.....,14,15
"""

#  Input Parameters
n1 = int(input("enter start num: "))
n2 = int(input("enter end num: "))

# NOTE:- do not change input parameters while performing some operation on them

i = n1
j = n2
while i <= j:
    print(i, end=" ")
    i += 1
