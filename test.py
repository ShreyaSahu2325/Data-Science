# ## Basic syntax Rules in python
# ## Case sensitivity

# Name="shreya"
# name="gupta"

# print(name)
# print(Name)

# age=32
# if age>30:
#     print(age)

# ## This is a single line comment
# print("Hello world")

# # Line continuation

# total=1+2+3+4+5+6+7+\
# 4+5+6
# print(total)

# ## Multiple statement on a single line

# x=5;y=10;z=x+y
# print(z)

# ## Understand semantic in python
# # variable assignment

# age=20; 
# name="shreya" 

# type(age)

# type(name)

# # Type inference

# variable=10
# print(type(variable))
# variable="krish"
# print(type(variable))

# age=32
# if age>30:
#     print(age)    

# ## code examples of indentation
# if True:
#     print("correct indentation")
#     if False:
#         print("This ont print")


    
#     print("This will print")
# print("This is my first python code")


# ##declaring and assigning variables
# age=20
# height=5.2
# name="shreya"
# is_student=True

# print("age",age)
# print("height",height)
# print("name",name)

# ##valid variation name
# first_name="shreya"
# last_name="gupta"

# #invaid variation name
# age2=20
# first_name="shreya"
# name="shreya"

# ##case sensetivity
# name="shreya"
# Name="shreya"
# name==Name
# ##understanding variable types

# #python is a dynamically type,type of a variable is determined at runtime

# age=20#int
# height=5.2#float
# name="shreya"#str
# is_student=True#bool

# print(type(age))
# print(type(height))
# print(type(name))

# ##Type checking and conversion

# type(height)
# ## one data type to another data type

# age=20
# print(type(age))

# #Type conversion

# age_str=str(age)
# print(age_str)
# print(type(age_str))

# ##Dynamic typing
# var=10#int
# print(var,type(var))

# var="Hello"
# print(var,type(var))

# var=3.14
# print(var,type(var))

# ##Type casting
# age=int(input("what is the age"))
# print(age)
# print(type(age))

# ##simple calculator

# num1=float(input("enter the first number"))
# num2=(float(input("enter the second number")))

# sum=num1+num2
# difference=num1-num2
# product=num1*num2
# quotient=num1/num2

# print("sum",sum)
# print("difference",difference)
# print("product",product)
# print("quotient",quotient)

# ##Integer example

# age=20
# Type(age)

# ##Floating point data type
# height=5.11
# print(height)
# print(Type(height))

# ##String data type example
# name="shreya"
# print(name)
# print(type(name))

# ##Boolan datatype
# Type(True)
# is_True=True
# Type(is_true)
# a=10
# b=10
# a==b
# type(a==b)

# ##common errors
# result="Hello" + str(5)
# print(result)

## Arithmatic operators
# a=10
# b=20
# add_result=a+b
# sub_result=a-b
# mult_result=a*b
# div_result=a/b
# floor_div_divison=a//b
# modulus_result=a%b
# exponent_result=a**b

# print(add_result)
# print(sub_result)
# print(modulus_result)
# print(modulus_result)
# print(exponent_result)
# print(floor_div_divison)
# print(exponent_result)

# ##comparison operators
# a=10
# b=10

# ## Not equal to
# str1="Shreya"
# str2="shreya"
# str!=str2

# ## Greater than

# num1=45
# num2=55

# num1>num2

# ##Less than
# num1=45
# num2=55

# num1<num2

# ##Greater than equal to
# num1=45
# num2=45

# num1>=num2

# ##Less than or equal to
# num1=45
# num2=45
# print(num1<=num2)

# ##Logical operator

# X=True
# Y=True

# result=X and Y
# print(result)

# X=False
# Y=False
# result= X or Y
# print(result)

# X=True
# not X


##if statement
age=20
if age>=18:
    print("you are allowed to vote in the elections")

##else statement

age=16
if age>=18:
    print("you are allowed to vote in the elections") 
else:
    print("you are not allowed to vote in the elections")


##elif statement
age=20
if age<13:
    print("you are a child")
elif age>=20:
    print("you are allowed to vote")
else:
    print("you are an adult")

##nested conditional statement

## number even,odd,negative
num=int(input("enter the number"))
if num>0:
    print("the number is positive")
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is negative")       

##leap year using nested if condition
year=int(input("enter the year"))

if year%4==0:
    if year%100:
        if year%400:
            print(year," is a leap year")
        else:
            print(year," is not leap year")
    else:
        print(year," is a leap year")    
else:
    (year," is not leap year")

    
                      