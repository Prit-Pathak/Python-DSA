my_string = "hyuhjhTYFTDKcyhb25743863^%%$%$^$##$ehjTFGYCfbjd"
count = 0
count1 = 0

# Method I
# for chr in my_string:
#     if ord(chr) in range(97, 122):
#         count += 1
#     elif ord(chr) in range(65, 90):
#         count1 += 1

# Method II
for chr in my_string:
    if "a" <= chr <= "z":
        count += 1
    elif "A" <= chr <= "Z":
        count1 += 1

print(count)
print(count1)
