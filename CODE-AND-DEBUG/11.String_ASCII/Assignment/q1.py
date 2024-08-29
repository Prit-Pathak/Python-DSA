# Method I
# def rev_str():
#     my_str = input("Enter the string :")
#     n = len(my_str)
#     rev_string = my_str[n - 1 :: -1]
#     return rev_string


# Method II
# def rev_str():
#     my_str = input("Enter the string :")
#     rev_string = my_str[::-1]
#     return rev_string


# Method II
def rev_str():
    my_string = input("eneter the string")
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


a = rev_str()
print(a)
