def oct2dec(x):
    n = len(x)
    result = 0
    for i in range(n):
        bit = int(x[i])
        result += bit * 8 ** (n - 1 - i)
    return result


if __name__ == "__main__":
    print(oct2dec("13042"))