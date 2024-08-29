my_str = "uheuhfiqojijijjjjjijwidh"
my_dict = {}

for ch in my_str:
    my_dict[ch] = my_dict.get(ch, 0) + 1

print(my_dict)
max_freq = 0
max_freq_ele = None
for keys, values in my_dict.items():
    if values > max_freq:
        max_freq = values
        max_freq_ele = keys

print(f"max freq ele is: {max_freq_ele} and freq is {max_freq} times")
