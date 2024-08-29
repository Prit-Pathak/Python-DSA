# function that replace all consonants in a given string with asterisks (*)


def is_asterisk(s: str) -> str:
    res = ""
    vow = "aeiouAEIUO"
    for ch in s:
        if ("a" <= ch <= "z" or "A" <= ch <= "Z") and ch not in vow:
            res += chr(42)
        else:
            res += ch
    return res


s = "Prit ts 888 office 6565"
a = is_asterisk(s)
print(a)
