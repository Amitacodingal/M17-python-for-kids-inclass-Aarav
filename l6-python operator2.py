# and or operator

a = 23
b = 24
c = 22


if a > b or a < c:
    print("I am using or operator")
elif a < b and a > c:
    print("I am using and operator")
    
# not equal to operator

a = 10
b = 12
c = 12

print(a != b)
print(b != c)


a = "python"
b = "coding"

if a != b :
    print(a, 'and', b, 'are different.')

a = 4
b = 5

if (a == 1) != (b == 5):
    print('Hello')

a = int(input("enter a number"))

if a%2 != 0 :
    print(a, "is not even number.")  
    
# BMI calculator

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
    


#ACP  weather enter text is character or not

# Take input from the user
char = input("Enter a character: ")

# Check if the character is an alphabet
if char.isalpha():
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")

 