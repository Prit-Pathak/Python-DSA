# python is a good language -> nohtyp si a doog egaugnal

s = "python is a good language"

rev = s.split()
res = ""
for item in rev:
    res += item[::-1]
    res += "-"

print(res[:-1])

# method 2

print(" ".join(word[::-1] for word in rev))
