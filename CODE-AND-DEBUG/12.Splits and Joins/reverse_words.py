# reverse word of the string
# python is a good language -> language good a is python

my_str = "python is a good language"

res = my_str.split()

res = res[::-1]

rev = " ".join(r for r in res)
print(rev)
