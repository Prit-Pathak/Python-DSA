# removes vowel from string (a,e,i,o,u)
def rm_vowl(my_str: str) -> str:
    no_vowels = ""
    vowels = "aeiouAEIOU"
    for ch in my_str:
        if ch not in vowels:
            no_vowels += ch

    return no_vowels


s = "prit's voice is a uniquie"
res = rm_vowl(s)
print(res)
