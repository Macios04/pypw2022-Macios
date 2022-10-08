def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        return "underweight"
    elif bmi > 20:
        return "overweight"
    return "normal"


if __name__ == "__main__":
    weight = float(input("weight: "))
    height = float(input("height: "))
    result = calculate_bmi(weight, height)
    print(f"Your status: {result}")