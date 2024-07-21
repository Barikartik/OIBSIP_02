def calculate_bmi(weight,height):
    return weight/(height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Over Weight"
    else:
        return "Obese"
    
def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight=float(input("Please Enter your weight in kilograms(kg)"))
        height=float(input("Please Enter your height in meters(m)"))
        if weight <=0 or height <=0:
            print("Weight and height must be positive numbers")    
            return 
    except ValueError:
        print("Invalid Input. Please enter numerical value for weight and height") 
        return

    bmi= calculate_bmi(weight,height)
    category= categorize_bmi(bmi)

    print(f"Your BMI is :{bmi:.2f}")
    print(f"Based on your BMI, you are classified as :{category}")
    Name=str(input("Enter your name"))
    print(f"Thankyou For Using {Name}")

if __name__== "__main__":
    main()
