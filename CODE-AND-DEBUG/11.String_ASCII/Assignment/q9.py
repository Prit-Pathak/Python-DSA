# function that count the number of digits in the given string


def count_num(s: str) -> int:
    count = 0
    for ch in s:
        ascii = ord(ch)
        if 48 <= ascii <= 57:
            count += 1
    return count


s = "prit is a 6647893y238 ujhfud9093irh827e812781"

a = count_num(s)
print(a)
