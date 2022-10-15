def is_lucky(num):
    p1 = int(num[0]) + int(num[1]) + int(num[2])
    p2 = int(num[3]) + int(num[4]) + int(num[5])
    if p1 == p2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(is_lucky("223214"))
    pass


def is_lucky_2(serial):
    first_part = [int(x) for x in serial[:3]]
    second_part = [int(x) for x in serial[3:]]
    return sum(first_part) == sum(second_part)

if __name__ == "__main__":
    print(is_lucky("112004"))
    pass

def create_lucky_tickets(n):
    result = []
    i = 0
    for i in range(10 ** 6):
        serial = str(i).zfill(6)
        if is_lucky(serial):
            result.append(serial)
        if len(result) >= n:
            break
    return result

if __name__ == "__main__":
    print(create_lucky_tickets(100))
    pass

def calculate_total_lucky_tickets():
    total = 0
    for i in range(10 ** 6):
        serial = str(i).zfill(6)
        if is_lucky(serial):
            total += 1
    return total

if __name__ == "__main__":
    print(calculate_total_lucky_tickets())
    pass
