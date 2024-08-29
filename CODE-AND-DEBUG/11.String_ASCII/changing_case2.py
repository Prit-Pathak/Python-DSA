# Swapcase
# uppercase -> lowercase
# lowercase -> uppercase
my_string = "bcwdjcnc^*T^&%kjdbiudbjsdc byiwdcbw%$^%"

res = ""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        ascii -= 32
        res += chr(ascii)
    elif ascii >= 65 and ascii <= 90:
        ascii += 32
        res += chr(ascii)
    else:
        res += ch
        # continue

print(res)
