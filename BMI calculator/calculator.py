def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        print("Height cannot be zero.")
        return None

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        bmi = calculate_bmi(weight, height)
        if bmi is not None:
            category = classify_bmi(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
