def solve_equation(a, b, c):
    d = (b ** 2 - 4 * a * c)
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    return (x1, x2)


if __name__ == "__main__":
    print(solve_equation(1, 1, 1))