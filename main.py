height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight/(height**2))

# print(bmi)

# print(round(bmi)) #Print 31 use round fn for decimal conversion

# print(round(bmi,2)) #Print 30.85

# F-string for print with type conversion
print(f"Your BMI is: {round(bmi,2)}kg")
