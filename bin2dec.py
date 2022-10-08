def bin2dec(x):
    n = len(x)
    result = 0
    for i in range(n):
        bit = int(x[i])
        result += bit * 2 ** (n - 1 - i)
    return result


if __name__ == "__main__":
    x = str(input("Enter: "))
    print(bin2dec(x))
