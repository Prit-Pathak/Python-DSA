"""
my_string
"""

# count alphabet, digits, spaces, and symbols
# a-z, A-Z,  0-9,


def count(my_string: str):
    alphabet = 0
    num = 0
    spaces = 0
    symbols = 0
    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code == 32:
            spaces += 1
        elif (97 <= ascii_code <= 122) or (65 <= ascii_code <= 90):
            alphabet += 1
        elif ascii_code >= 48 and ascii_code <= 57:
            num += 1
        else:
            symbols += 1
    print(f"alphabet : {alphabet} num : {num} symbols : {symbols} spaces : {spaces}")


my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"

count(my_string)
