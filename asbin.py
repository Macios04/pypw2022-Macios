def as_bin(x):
    result = ""
    if x == 0:
        return "0"
    while x != 0:
        x, bit = divmod(x, 2)
        result = str(bit) + result
    return result

if __name__ == "__main__":
    print(as_bin(150))






