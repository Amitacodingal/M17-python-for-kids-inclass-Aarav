#first lesson flow chart and algorithm docs link 
# https://docs.google.com/document/d/1JdkyRpccUIoLy_3ecrjqqNcnGEgk8BX9gKbiYmuZjDM/edit?usp=sharing

#lesson 3 Discussed about what are datatypes, 
#typecasting means converting one dataype to other 
#how to take user input and perform string operations

# Let's check the datatype of different values we can do that with type()
a = 10
print("type of a: ", type(a))

b=72.5
print("type of b: ", type(b))

c= "Love Coding"
print("type of c: ", type(c))

d= True
print("type of d: ", type(d))


# -------------------------------------------------------------------

# Assigning Different Variables
name = "Aarav"
age = 12
is_present = True
weight = 30.5

# Printing Different Variables and their Data Type
print("Name :", name)
print("Data Type of Name is", type(name))

print("Age :", age)
print("Data Type of Age is", type(age))

print("is student present :", is_present)
print("Data Type of is_present is", type(is_present))

print("Weight :", weight)
print("Data Type of weight is", type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))

#when we type cast we loose some data. 