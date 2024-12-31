"""Write a program that calculates the BMI (Body Mass Index) and categorizes it based on the following:
BMI < 18.5: Underweight
18.5 <= BMI < 25: Normal weight
25 <= BMI < 30: Overweight
BMI >= 30: Obesity"""

weight= float(input("enter your weight in kg: "))
height= float(input("enter your height in m: "))

BMI= weight/(height**2)
print("Calculated BMI:",BMI)

if BMI<18.5:
    print("Underweight")
elif 18.5<=BMI<25:
    print("Normal weight")
elif 25<=BMI<30:
    print("Overweight")
else:
    print("Obesity")

