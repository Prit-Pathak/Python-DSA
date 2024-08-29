"""
Ask a string from user. Store the frequency of each character in the
dictionary. Then print the character with the maximum frequency.
i/p -> enter a string: hello world
o/p -> The character with the maximum frequency is 'l'
"""

char = input("enter character: ")
my_dict = {}

for ch in char:
    my_dict[ch] = my_dict.get(ch, 0) + 1

print(my_dict)
max_freq = 0
max_freq_ele = None
for keys, values in my_dict.items():
    if values > max_freq:
        max_freq = values
        max_freq_ele = keys

print(max_freq_ele)
