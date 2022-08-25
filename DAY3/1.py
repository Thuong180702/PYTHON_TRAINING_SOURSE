Hight = int(input("Enter your hight in m: "))
Weight = float(input("Enter your weight in kg: "))

BMI = Hight / Weight ** 2

if BMI < 18.5:
    print(f"Your bmi is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your bmi is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your bmi is {BMI}, you are overweight.")
elif BMI < 35:
    print(f"Your bmi is {BMI}, you are obese.")
else:
    print(f"Your bmi is {BMI}, you are clinically obese.")
