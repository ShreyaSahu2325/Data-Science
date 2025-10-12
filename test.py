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


# ##if statement
# age=20
# if age>=18:
#     print("you are allowed to vote in the elections")

# ##else statement

# age=16
# if age>=18:
#     print("you are allowed to vote in the elections") 
# else:
#     print("you are not allowed to vote in the elections")


# ##elif statement
# age=20
# if age<13:
#     print("you are a child")
# elif age>=20:
#     print("you are allowed to vote")
# else:
#     print("you are an adult")

# ##nested conditional statement

# ## number even,odd,negative
# num=int(input("enter the number"))
# if num>0:
#     print("the number is positive")
#     if num%2==0:
#         print("number is even")
#     else:
#         print("number is odd")
# else:
#     print("number is negative")       

# ##leap year using nested if condition
# year=int(input("enter the year"))

# if year%4==0:
#     if year%100:
#         if year%400:
#             print(year," is a leap year")
#         else:
#             print(year," is not leap year")
#     else:
#         print(year," is a leap year")    
# else:
#     (year," is not leap year")


# ##for loop 

# for i in range(5):
#      print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(10,1,-1):
#   print(i)


# ## strings
# str="shreya gupta"
# for i in str:
#     print(i)

# ## while loop

# count=0
# while count<5:
#    print(count)
#    count=count+1

# count=0
# while count%2==0:
#     print(count)
#     count=count+1
     
# ## break statement
# for i in range(10):
#     if i==5:
#         break
#     print(i)


# ## continue statement

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# ## pass statement

# for i in range(5):
#     if i==3:
#         pass
#     print(i)

# ## nested loop
# for i in range(3):
#     for j in range(2):
#         print(f"i:{i} and j:{j}")

# ## example
# n=10
# sum=0
# count=1

# while count<=n:
#     sum=sum+count
#     count=count+1
# print("sum of the first 10 natural number: ", sum)


# #for loop

# n=10
# sum=0
# count=1

# for i in range(11):
#     sum=sum+i

# print(i)

# # for loop
# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num) 


# ## List
# lst=[]
# print(type(lst))

# names=["shreya","jack","aditri"]
# print(names)

# Mixed_list=[1,"Hello",3.14,"True"]
# print(Mixed_list)
# print(type(Mixed_list))

# ## Accessing list elements

# fruits=["Apple","Banana","cherry","kiwi","Grapes"]
# print(fruits[0])
# print(fruits[2])
# print(fruits[-1])
# print(fruits[1:])
# print(fruits[1:3])
# print(fruits[-1:-4])

# ## Modifying the list elements
# fruits=["Apple","banana","kiwi","cherry","grapes"]
# fruits[1]="watermelon"
# print(fruits)

# ## list method
# fruits=["Apple","banana","kiwi","cherry","grapes"]
# fruits.append("orange")
# print(fruits)

# fruits.insert(1,"coconut")
# print(fruits)

# fruits.remove("grapes")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.index("cherry")
# fruits.insert(2,"banana")
# print(fruits.count("banana"))
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits)

# ## slicing list
# numbers=[1,2,3,4,5,6,7,8,9]
# print(numbers[2:5])

# print(numbers[5 :])
# print(numbers[: : 2])
# print(numbers[: : -1])

# ## iterating over list
# for number in numbers:
#     print(number)

# ## indexing with list
# for index , number in enumerate(numbers):
#     print(index,number)


# ## list comprehension
# lst=[]
# for x in range(10):
#     lst.append(x**2)

# print(lst)

# [x**2 for x in range(10)]

# ##list comprehension

# #basic syntax
# #with conditional logic


# square=[num**2 for num in range(10)]
# print(square)

# ## list comprehension with conditional 
# for i in range(10):
#     if i%2==0:
#         print(lst.append(i))

# print(lst)

# even_numbers=[num for num in range(10) if num%2==0]
# print(even_numbers)

# ## nested list comprehension
# lst1=[1,2,3,4]
# lst2=["a","b","c","d"]

# pair=[[i,j] for i in lst1 for j in lst2 ]
# print(pair)

# ## list comprehension with function calls

# words=["hello","world","python","list"]

# lengths=[len(word) for word in words]
# print(lengths)

# ## creating Tuple
# empty_tuple=()
# print(empty_tuple)
# print(type(empty_tuple))

# lst=list()
# print(type(lst))
# tpl=tuple()
# print(type(tpl))

# numbers=tuple([1,2,3,4,5])
# print(numbers)

# lst=list((1,2,3,4,5))
# print(lst)


# mixed_tuple=(1,"Hello world",3.14,True)
# print(mixed_tuple)

# ## Accessing Tuple elements
# numbers=[1,2,3,4,5]
# print(numbers[2])
# print(numbers[-1])
# print(numbers[0:4])

# numbers=[1,2,3,4,5,6]
# print(numbers)

# mixed_tuple * 3
# print(mixed_tuple)

# ## immutable nature of tuples

# lst=[1,2,3,4,5]
# print(lst)

# lst[1]="shreya"
# print(lst)

# numbers=[1,2,3,4,5]
# numbers[1]="shreya"

# ## tuple method
# print(numbers.count(1))
# print(numbers.index(3))

# ## packing and unpacking tuple
# packed_tuple=1,"Hello",3.14
# print(packed_tuple)

# a,b,c=packed_tuple
# print(a)
# print(b)
# print(c)

# ## unpacking with *
# names=("jack","krish","adver")
# first,*middle,last=names
# print(first)
# print(middle)
# print(last)

# ## NESTED tuple
# # nested list
# lst=[[1,2,3],[5,6,7],(5,"hello","c")]
# lst[2]

# ## access the element inside a tuple
# nested_tuple=((1,2,3),("a","b","c"),(True,False))
# print(nested_tuple[2])

# print(nested_tuple[1][2])

# ## iterating over nested tuple

# for sub_tuple in nested_tuple:
#     for item in sub_tuple:
#         print(item,end=" ")
#     print()    


# ## create a set
# my_set={1,2,3,4,5}
# print(type(my_set))

# my_empty_set=set()
# print(my_empty_set)

# my_set={1,2,3,4,5}
# print(my_set)

# my_set={1,2,3,4,5,6,6,5}
# print(my_set)

# ## basic sets operation
# #3 adding and removing element

# my_set=set([1,2,3,4,5,6])
# my_set.add(7)
# print(my_set)
# my_set.remove(3)
# print(my_set)

# ## pop method
# removed_element=my_set.pop
# print(removed_element)
# print(my_set)

# fruits={"apple","banana","cherry"}
# items=fruits.pop()
# print(items)
# print(fruits)

# ## clear all the elements
# my_set={1,2,3,4,5}
# my_set.clear()
# print(my_set)

# my_set={1,2,3,4,5,6}
# print(3 in my_set)
# print(10 in my_set)

# ## mathematical operation
# set1={1,2,3,4,5}
# set2={4,7,8,9,3}
# union_set=set1.union(set2)
# print(union_set)

# ## intersection set
# set1={1,2,3,4,5}
# set2={2,1,4,5,6,8}
# intersection_set=set1.intersection(set2)
# print(intersection_set)

# ## difference
# set1={1,2,3,4,5,6,7}
# set2={2,3,4,9,8}
# print(set1.difference(set2))
# set.difference_update(set2)
# print(set1)

# set2.difference(set1)

# set={1,2,3,4,5}
# set2={2,3,4,7,8,9}
# print(set1.symmetric_difference(set2))

# ## sets method
# set1={1,2,3}
# set2={3,4,5}
# ## is subset
# print(set1.issubset(set2))


# ## create dictionaries
# empty_dict={}
# print(type(empty_dict))

# empty_dict=dict()
# print(empty_dict)

# student={"name":"shreya","age": 20, "grade": 24}
# print(student)

# # error
# student={"name":"shreya","age": 20,"name":"shreya"}
# print(student)

# ## accessing dictionary elements
# student={"name":"shreya","age": 20, "grade" :"A"}
# print(student["grade"])
# print(student["name"])
# print(student["age"])


# ## accessing using get() method

# student={"name":"shreya","age":20,"grade":"A"}
# print(student.get("grade"))
# print(student.get("last_name"))
# print(student.get("last_name","not available"))

# ## modifying dictionary element

# student={"name":"shreya","age":20,"grade":"A"}
# student["age"]=33
# print(student)
# student["address"]="india"
# print(student)

# del student["grade"]
# print(student)

# ## dictionary method
# keys=student.keys()
# print(keys)

# values=student.values()
# print(values)

# items=student.items()
# print(items)

# ## shallow copy
# student_copy=student
# print(student)
# print(student_copy)

# student["name"]="shreya2"
# print(student)
# print(student_copy)

# ## iterating over dictionaries
# for keys in student.keys():
#     print(keys)

# ## Iterating over values
# for values in student.values():
#     print(values)


# ## itearte over key value pairs

# for key,value in student.items():
#     print(f"{key} :{value}")

# ## nested dictionary

# students={
#     "student" : "jack", 
#     "age" : 20,
#     "score" : 90
# }
# print(students)

# print(students["student"],["name"])
# print(students["age"])

# ##access nested dictionary elements
# students={
#     "student1" : {"name" : "shreya", "age" : 20},
#      "student2" : {"name" : "peter" ,"age" :35}
#  }

# print(students["student2"]["name"])
# print(students["student2"]["age"])
# students.items()
# ## iterating over nested dictionary

# for student_id, student_info in student.items ():
#     print(f"{student_id}:{student_info}")
#     for key,value in student.items():
#         print(f"{key}:{value}")


# ## dictionary comprehension
# squares={x:x**2 for x in range(5)}
# print(squares)

# ## conditional dictionary comprehension

# evens = {x:x**2 for x in range(10) if x%2==0}
# print(evens)

# ## merged dictionary
# dict1={"a":1 ,"b":2}
# dict2={"c" :3 , "d" :4 }
# merged_dict={**dict1,**dict2} 
# print(merged_dict)

# #manage A TO Do List
# ## create a to_Do_list to keep track of tasks
# To_do_list=["buy Grocries","clean the house","pay bill"]
# #Adding the task
# To_do_list.append("schedule meeting")
# To_do_list.append("go for a run")

# ## Removing the completed task

# To_do_list.remove("clean the house")

# ##checking if a task is in the list

# if "pay bill" in To_do_list:
#     print("Don't forget to pay the utility bills")

# print("To do list remaing")
# for task in To_do_list:
#     print(f"{task}")


# ## organizing student grades
# grades=[85, 78,  98, 67, 97]

# ## Adding a new grade
# grades.append(99)

# ## calculating the average grade 

# average_grade = (sum(grades) / len(grades))
# print(f"Average grade : {average_grade:.2f}")

# # find the highest grades
# highest_grade=max(grades)
# lowest_grade=min(grades)
# print(f"Highest grade :{highest_grade}")
# print(f"lowest grade :{lowest_grade}")


# # use a list to maange inventory items in a stock

# ## managing in a inventory
# inventory=["apple","bananas","oranges","grapes"]

# ## adding a new items
# inventory.append("mangos")

# ## removing the items that is out of stock
# inventory.remove("bananas")

# ## checking if an items is in stock
# items="oranges"
# if items in inventory:
#     print(f"{items} is in stock")

# else:
#     print(f"{items} is out of stock")

# ## printing the inventory
# print("inventory list : ")
# for item in inventory:
#     print(f"-{items}")
    
#collecting user service
# # feedback=["Great service!" ,"very satisfied" ,"could be better","excellent experience"]


# # ## adding a new feedback
# # feedback.append("not happy with the service")

# # ## removing the items that is out of stock
# # inventory.remove("bananas")

# # ## counting specific feedback
# # positive_feedback_count= sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower())
# # print(f"positive feedback count :{positive_feedback_count}")

# # ## printing all feedback
# # print("user feredback")
# # for comment in feedback:
# #     print(f"-{comment}")

## Function in python
#syntax
def function_name(parameters):
    """Docstring"""
    ##Function body
    return 

## why function
num=24
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

def even_or_odd(num):
    """This function finds even or odd"""
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

## call this function
even_or_odd(23)

## function with multiple parameters

def add(a,b):
    return a+b

result=add(2,4)
print(result)

## default parameters

def greet(name="Guest"):
    print(f"{name} Welcome to the paradise")

greet()


def greek(name="Guest"):
    print(f"{name} welcome to my channel")

greek()

## variable length arguments
# postional and keyword argument

def print_numbers(*args):
    for number in args:
        print(number)
 
# call this function
print_numbers(1,2,3,4,5,6,8,"shreya")

## keywords arguments

def print_details(** kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="shreya",age=20,country="india")

def print_details(*args,**kwargs):
    for val in args:
        print(f"positional arguments :{val}")
    
    for key,value in kwargs.items():
        print(f"{key}:{value}")

## call this function
print_details(1,2,3,4,5,name="shreya",age=20,country="india")

## return statement

def multiply(a,b):
    return a*b,a

## call this function
multiply(2,3)



