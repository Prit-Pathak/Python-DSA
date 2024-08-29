# function that checks if a given string contains only alphanumeric characters


def alpha_num(s: str) -> bool:
    for ch in s:
        if not (("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9")):
            return False
    return True


s = "iejfmf43544mkewfk0eewofmkm$%^&"

z = alpha_num(s)
print(z)
