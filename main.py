print("Welcome to the BMI Calculator")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#  calculate bmi - BMI = Weight (kg) / Height (m)²  

bmi = weight / (height * height);
bmi_as_a_int = round(bmi)

 # if statement to determine interpretation of their BMI based on the BMI value
if bmi < 18.5:
  print(f"Your BMI is {bmi_as_a_int}, you are underweight.")
elif 18.5 < bmi <= 25:
    print(f"Your BMI is {bmi_as_a_int}, you are a normal weight.")
elif 26 < bmi <=30 :
    print(f"Your BMI is {bmi_as_a_int}, you are slightly overweight.")
elif 30 < bmi <=34 :
    print(f"Your BMI is {bmi_as_a_int}, you are obese.")
 
else:
      print(f"Your BMI is {bmi_as_a_int}, you are clinically obese.")


