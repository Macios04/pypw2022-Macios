def hex2dec(x):
    mapping = {
        "A": 10, "B": 11, "C": 12,
        "D": 13, "E": 14, "F": 15,
    }
    return sum([
        int(mapping.get(val, val)) * 16 ** pos
        for pos, val in enumerate(reversed(x))
        if val != "0"
    ])

if __name__ == "__main__":
    print(hex2dec("FF"))
