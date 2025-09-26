## Basic syntax Rules in python
## Case sensitivity

Name="shreya"
name="gupta"

print(name)
print(Name)

age=32
if age>30:
    print(age)

## This is a single line comment
print("Hello world")

# Line continuation

total=1+2+3+4+5+6+7+\
4+5+6
print(total)

## Multiple statement on a single line

x=5;y=10;z=x+y
print(z)

## Understand semantic in python
# variable assignment

age=20; 
name="shreya" 

type(age)

type(name)

# Type inference

variable=10
print(type(variable))
variable="krish"
print(type(variable))

age=32
if age>30:
    print(age)    

## code examples of indentation
if True:
    print("correct indentation")
    if False:
        print("This ont print")


    
    print("This will print")
print("This is my first python code")


##declaring and assigning variables
age=20
height=5.2
name="shreya"
is_student=True

print("age",age)
print("height",height)
print("name",name)

##valid variation name
first_name="shreya"
last_name="gupta"

#invaid variation name
2age=20
first-name="shreya"
@name="shreya"

##case sensetivity
name="shreya"
Name="shreya"
name==Name
##understanding variable types

#python is a dynamically type,type of a variable is determined at runtime

age=20#int
height=5.2#float
name="shreya"#str
is_student=True#bool

print(type(age))
print(type(height))
print(type(name))

##Type checking and conversion

type(height)
## one data type to another data type

age=20
print(type(age))

#Type conversion

age_str=str(age)
print(age_str)
print(type(age_str))

##Dynamic typing
var=10#int
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))

##Type casting
age=int(input("what is the age"))
print(age)
print(type(age))

##simple calculator

num1=float(input("enter the first number"))
num2=(input(int("enter the second number")))

sum=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2

print("sum",sum)
print("difference",difference)
print("product",product)
print("quotient",quotient)