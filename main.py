w = int(input("enter weight in kg"))
h = float(input("enter hight in meters "))
bmi = w/h**2
if bmi<18.5:
    print("underweight")
if 18.5 <= bmi < 24.9 :
    print("normal weight ")
if 25 <= bmi< 29.9:
    print("overweight")
if bmi >= 30 :
    print("obesity")

    





