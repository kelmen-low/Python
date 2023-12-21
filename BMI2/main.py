weight = float(input("What is your weight in kg?: "))
height = float(input("What is you height in meters?: "))

BMI = weight / height ** 2

if BMI < 18.5:
    print("You are under weight")
elif BMI <=24.9:
    print("You are a healthy weight")
elif BMI <= 29.9:
    print("You are over weight")
else:
    print("You are obese")
