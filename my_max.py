def my_max(a, b):
    if a > b:
        return a
    if b > a:
        return b
    else:
        return "even"

if __name__ == "__main__":
    print(my_max(10, 0))
    pass

def my_max3(a, b, c):
    return max([a, b, c])

if __name__ == "__main__":
    print(my_max3(1, 999, 222))
    pass

def minmax(list):
    result = (min(list), max(list))

if __name__ == "__main__":
    print(minmax([2, 3, 4, 5]))
    pass


