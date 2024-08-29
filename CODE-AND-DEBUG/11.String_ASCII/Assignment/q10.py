# function to remove duplicate string from the given string.


def rm_dup(s: str) -> str:
    res = ""
    for ch in s:
        if ch not in res:
            res += ch

    return res


s = "periueuinejiooooo[pprkekofkfkkfk]"

z = rm_dup(s)
print(z)
