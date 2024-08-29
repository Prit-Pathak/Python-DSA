# count the number of words in a given string
def count_str(my_str: str) -> int:
    if not my_str:
        return 0
    count = 1
    for ch in my_str:
        if ord(ch) == 32:
            count += 1
    return count


s = "Prit is a good boy"

res = count_str(s)
print(res)
