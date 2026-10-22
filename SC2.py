#Name:
#Class: 5th Hour
#Assignment: SC2

#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

weight = float(input("Enter Weight in Kg: "))
height = float(input("Enter Height in m: "))
print(weight)
print(height)

BMI = (weight / (height ** 2))


if 18.5>BMI:
    print("You are underweight")
elif 18.5<=BMI and 25>=BMI:
    print("You are normal weight")
elif 25<=BMI and 29.9>=BMI:
    print("You are overweight")
elif BMI>=30:
    print("You are obese")

print(BMI)