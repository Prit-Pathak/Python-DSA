# function that removes all non-alphabet from the string


def non_alpha(s: str) -> str:
    non_al_str = ""
    for ch in s:
        if "a" <= ch <= "z" or "A" <= ch <= "Z":
            non_al_str += ch
    return non_al_str


s = "Prit uis 7675 udhfb 877666h jhcuiha"
z = non_alpha(s)
print(z)
