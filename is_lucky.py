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

def is_lucky_gen(nums, n):
