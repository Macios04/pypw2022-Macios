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
    return result

if __name__ == "__main__":
    print(minmax([2, 3, 4, 5]))
    pass
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

if __name__ == "__main__":
    print(my_abs(-5))
    pass

def filter_nums(list):       #nie działa
    i = 0
    result = []
    for i in range(len(list)):
        if list[i] % 3 != 0:
            result.append(list[i])
            i += 1
        else:
            pass
    return result

if __name__ == "__main__":
    print(filter_nums([3, 4, 5, 7, 6, 9, 8, 22, 33, 69]))
    pass

def generate_evans(start, end):  #nie dziala
    i = 0
    list1 = list(range(start, end))
    result = []
    for i in range(len(list1)):
        if list1[i] % 2 == 0:
            result.append(list1[i])
            i += 1
        else:
            pass
    return result

if __name__ == "__main__":
    print(generate_evans(1, 12))
    pass

def compute(nums, n, m):
    i = 0
    result = []
    for i in range(len(nums)):
        result.append((nums[i] ** n) % m)
        i += 1
    return result

if __name__ == "__main__":
    print(compute([2, 3, 4, 12], 2, 3))
    pass



