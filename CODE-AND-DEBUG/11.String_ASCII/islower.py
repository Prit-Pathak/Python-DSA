# Method I -> Brute force approach
# def is_lower(my_string: str) -> bool:
#     alpha_str = []
#     for ch in my_string:
#         if ord(ch) in range(65, 90) or ord(ch) in range(97, 122):
#             alpha_str.append(ch)
#         else:
#             continue
#     # print(alpha_str)
#     for item in alpha_str:
#         if ord(item) in range(97, 122):
#             return True
#     return False


# Method II -> Optimized Approach
def is_lower(my_string: str) -> bool:
    is_lower = False
    is_upper = False

    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            is_lower = True
        elif ascii_code >= 65 and ascii_code <= 90:
            is_upper = True

    # if is_lower == True and is_upper == False:
    #     return True

    if is_lower and not is_upper:
        return True
    return False


my_string = "hgfyedbAfuj23335$%(*)^"
a = is_lower(my_string)
print(a)
