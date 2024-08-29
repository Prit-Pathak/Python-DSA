# list slicing

my_lst = [33, 44, 55, 667, 8, 9, 3, 11]

x = my_lst[0:4]  # this is called slicing, works sililar to for loop

print(x)

y = my_lst[0:7:2]  # here , 2 is the step, like it will srep upby 2
print(y)

z = my_lst[3:]
print(z)

p = my_lst[:]
print(p)

r = my_lst[::2]
print(r)

n = my_lst[::-1]
print(n)

f = my_lst[5:2:-1]
print(f)

f = my_lst[5:-1:-1]
print(f)
