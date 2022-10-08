def dec2bin(x):
    n = len(x)
    s = 0
    for i in range(n):
        bit = int(x[i])
        s += bit * 2 ** (n - 1 - i)
    return s


if __name__ == "__main__":
    print(dec2bin("1111"))
