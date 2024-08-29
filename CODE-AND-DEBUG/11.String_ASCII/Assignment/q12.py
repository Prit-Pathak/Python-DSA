# function that replaces all the spaces in the given string with hyphens (-)
def rm_sp(s: str) -> str:
    res = ""
    for ch in s:
        if ch == " ":
            res += chr(45)
        else:
            res += ch
    return res


s = "jehujn mjdkk ojdikdij prijt"

z = rm_sp(s)
print(z)
