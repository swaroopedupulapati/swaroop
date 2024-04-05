def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")
    print("=============================")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    bmi_category = interpret_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"This is considered: {bmi_category}")

if __name__ == "__main__":
    main()
