def bin2dec(x):
    return sum([
        2 ** pos for pos, bit in enumerate(reversed(x))
        if bit == "1"
    ])
print(bin2dec("1010"))