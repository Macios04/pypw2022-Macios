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
    return my_max(my_max(a, b), c)

if __name__ == "__main__":
    print(my_max3(1, 999, 222))
    pass

def minmax(list):
    min_value = 0
    max_value = 0
    for item in list[1:]:
        if item >= max_value:
            max_value = item
        if item < min_value:
            min_value = item
    return min_value, max_value

if __name__ == "__main__":
    print(minmax([2, 3, 4, 5]))
    pass

def sweap(items):
    min_idx, max_idx = 0, 0
    for i in range(len(items)):
        if items[i] >= items[max_idx]:
            max_idx = i
        if items[i] < items[min_idx]:
            min_idx = i
    items[min_idx], items[max_idx] = items[max_idx], items[min_idx]
    return items

if __name__ == "__main__":
    print(sweap([2, 3, 4, 5]))
    pass

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

if __name__ == "__main__":
    print(my_abs(-5))
    pass

def filter_nums(list):
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

def generate_evans(start, end):
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

def compute_2(nums, n, m):
    return [x ** n % m for x in nums]

if __name__ == "__main__":
    print(compute_2([2, 3, 4, 12], 2, 3))

