
print("================================")
print("       BMI CALCULATOR")
print("================================")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values.")

    else:
        bmi = weight / (height * height)

        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("BMI Category:", category)

except ValueError:
    print("Error: Please enter valid numeric values.")
