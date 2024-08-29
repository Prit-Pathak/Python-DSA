# Split -> String to list
# Join -> List to string

s = ["P", "R", "I", "T"]

res = " ".join(ch for ch in s)
print(res)

res = "".join(ch for ch in s)
print(res)

res = "-".join(ch for ch in s)
print(res)

# result = "".join(ch for ch in my_list)
# result = "-".join(ch + "5" for ch in my_list)
# print(result)
# my_list = ["a", 4, 5, 6, 7, 8, 7, "Anirudh", "x", "y", "z"]

# print("".join(str(ch) for ch in my_list))
