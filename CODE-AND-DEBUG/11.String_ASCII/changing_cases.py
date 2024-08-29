my_str = "adbhbjdbCFDRFJnkjfikdn"

res = ""

for ch in my_str:
    ascii = ord(ch)

    if ascii >= 97 and ascii <= 122:
        ascii -= 32
        res = res + chr(ascii)
    else:
        res += ch

print(res)
