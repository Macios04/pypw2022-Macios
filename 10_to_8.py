def dec2oct(x):
    result = ""
    if x == 0:
        return "0"
    while x != 0:
        x, bit = divmod(x, 8)
        result = str(bit) + result
    return result


if __name__ == "__main__":
    print(dec2oct(700))