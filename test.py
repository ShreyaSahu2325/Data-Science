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
print("outside the if block")        
