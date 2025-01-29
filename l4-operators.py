
# what are operators how many types of operators are their
#artihmetic, comparission and assignment operartors
# Storing Values
tree1 = 98
tree2 = 94
tree3 = 41
tree4 = 95
tree5 = 11

# Finding the total of trees
sum = tree1+tree2+tree3+tree4+tree5
print("the sum of all the 5 trees is: ", sum)

# Finding the average of trees
average = sum/5
print("the average of all the tree is :", average)



#second activity 

# Taking total amount as input from user
Amount =int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominations
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10


print( "notes of 100 rupee" , note1)
print("notes of 50 rupee" , note2)
print("notes of 10 rupee" , note3)


#calcualte % of marks obatained by student

# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

# Let's calculate the percentage of marks
sum = math+english+science+hindi
print("sun of math,english,science and hindi")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)



# coverting the days
print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total Number of Year(s): ")
print(year)
print("Total Number of Week(s):")
print(week)
print("Total Number of Day(s):")
print(days)

#ACP 

# Input number
number = 25

# Calculate square root using exponentiation
sqrt_value = number ** 0.5

# Output the result
print(f"The square root of {number} is {sqrt_value}")



