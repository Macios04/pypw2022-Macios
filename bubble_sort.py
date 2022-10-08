def bubble_sort(items):
    right = len(items)
    run = True
    while run:
        run = False
        for i in range(right - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                run = True
        right -= 1
    return items

if __name__ == "__main__":
    result = bubble_sort([100, 20, 2, 4, 0, 1, 22,])
    print(result)


