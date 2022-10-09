def dec2hex(x):
    hexdic = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    result = ""
    if x == 0:
        return "0"
    while x != 0:
        x, reminder = divmod(x, 16)
        if reminder < 10:
            result = str(reminder) + result
        else:
            result = hexdic[reminder] + result
    return result

if __name__ == "__main__":
    print(dec2hex(255))

