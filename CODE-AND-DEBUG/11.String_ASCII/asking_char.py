"""
keep on asking characters from the user.
stop it untill he/she presses q.

enter char = e
enter char = g
enter char = s
enter char = p
enter char = q

o/p:-> "egspq"
"""


def ask_char() -> str:
    res = ""
    while True:
        my_chr = input("enter string : ")

        if my_chr == "q" or my_chr == "Q":
            break

        res += my_chr
    return res


a = ask_char()
print(a)
