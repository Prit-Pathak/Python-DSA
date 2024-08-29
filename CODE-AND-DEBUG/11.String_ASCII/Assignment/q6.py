# function that capitalizes first letter of each word in a given string.
def caps_word(s: str) -> str:
    wrd = ""
    res = ""

    for ch in s:
        if ch == " ":
            if wrd:
                res += chr(ord(wrd[0]) - 32) + wrd[1:]
            wrd = ""
        else:
            wrd += ch
    if wrd:
        res += chr(ord(wrd[0]) - 32) + wrd[1:]

    return res


s = "prit"
a = caps_word(s)
print(a)

"""
Method 2
"""


def capitalize(s: str) -> str:
    result = ""
    is_new_word = True
    for char in s:
        if is_new_word and "a" <= char <= "z":
            result += chr(ord(char) - 32)
            is_new_word = False
        else:
            result += char
        if char == " ":
            is_new_word = True
    return result


my_string = "python is a very easy coding language to learn"
print(capitalize(my_string))
