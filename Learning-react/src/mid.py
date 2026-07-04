def bmi_category(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        return("Underweight")
    elif bmi < 25:
        return("Normal")
    elif bmi < 30:
        return("Overweight")
    else:
        return("Obese")

print(bmi_category(150, 1.70))