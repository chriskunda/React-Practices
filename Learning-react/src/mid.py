def bmi_category(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

bmi_category(150, 1.70)