# python is a good language -> egaugnal doog a si nohtyp

s = "python is a good language"

res = s.split()
res = res[::-1]

res = " ".join(word[::-1] for word in res)

print(res)
