def bin2dec(x):
    n = len(x)
    s = 0
    for i in range(n):
        bit = int(x[i])
        s += bit * 2 ** (n - 1 - i)
    return s


if __name__ == "__main__":
    x = str(input("Enter: "))
    print(bin2dec(x))
