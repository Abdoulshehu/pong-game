print("BMI CALCULATOR!")
height = float(input("Enter Your Height__ "))
weight = float(input("Enter Your Weight__ "))

bmi = weight/height
if bmi <= 18.5 : 
    print("Underweight")
elif bmi > 18.5 and bmi <= 25 :
    print("Normal weight")
elif bmi > 25 and bmi <= 30 :
    print("Over weight")
elif bmi > 30 : 
    print(" Obese")
 
