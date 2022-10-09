def merge(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

a = [1, 3, 5, 8, 20, 55, 90, 1002]
b = [2, 4, 6, 9, 12, 13, 15, 86, 675]

if __name__ == "__main__":
    print(merge(a, b))