def oct2dec(x):
    return sum([
        int(val) * 8 ** pos for pos, val in enumerate(reversed(x))
        if val != "0"
    ])
print(oct2dec("1213"))