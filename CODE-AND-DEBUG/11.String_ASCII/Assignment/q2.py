#  Method I
# def is_upper(my_str: str) -> str:
#     upper_str = ""
#     for ch in my_str:
#         asci = ord(ch)
#         if 97 <= asci <= 122:
#             asci -= 32
#             upper_str += chr(asci)
#         else:
#             upper_str += ch
#     return upper_str


# Method II
def is_upper(my_str: str) -> str:
    upper_str = ""
    for ch in my_str:
        if "a" <= ch <= "z":
            upper_str += chr(ord(ch) - 32)
        else:
            upper_str += ch
    return upper_str


my_str = "dhgyewbfjRTFIVYIB73678mknojadh"
res = is_upper(my_str)
print(res)
