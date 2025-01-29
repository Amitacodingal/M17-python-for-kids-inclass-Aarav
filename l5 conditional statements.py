# ACP 
# write a program in python check what temperature is suitable for wearing light clothes.

temp = float(input("Enter the current temperature in Celsius: "))
if temp >= 18:
        return "It's warm enough to wear light clothes."
else:
        return "It's too cold for light clothes. Wear something warmer."


#activity 1 weather a number is positive or not

n=int(input("Enter the number:"))
if( n%2==0 ):
  print("The number is even")
else:
  print("The number is odd")
  
#activity 2 weather a number is even or odd
  
num = int(input("Enter a number: "))
if num > 0:
    print("The Number is positive number")
    
#activity 3 

actual_cost = float(input(" Please Enter the Actual Product Price: ") )
sale_amount = float(input(" Please Enter the Sales Amount: ") )

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = ", amount)
else:
    print("No Profit! !! ")

# weather a number is greater or smaller
i = int(input("enter a number : ") )
if (i < 15):
    print ("i is smaller than 15")
    print ("i'm in if Block")
else:
    print ("i is greater than 15")
    print ("i'm in else Block")
    print ("i'm not in if and not in else Block")
