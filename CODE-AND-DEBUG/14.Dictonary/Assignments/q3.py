sub = ["maths", "phy", "che", "sst"]
marks = [99, 85, 65, 70]

n = len(sub)
my_dict = {}
for i in range(n):
    my_dict[sub[i]] = marks[i]

print(my_dict)
