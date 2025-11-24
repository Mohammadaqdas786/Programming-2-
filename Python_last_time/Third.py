# marks = [98.4, 100, 50, 40, 78]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[2])
#
#
# student = ["karan ", 100,"male"]
# print(student)
# print(type(student))
# print(student[0])
from kivy.core import handle_win_lib_import_error
from unicodedata import digit

# List and tuples
# friends = ["Apple", "orange", 5,67,88, False,"akn", "fernod"]
# friends[0] = "Me"
# print(friends)
# friends.append("harry")
# print(friends)


# l1 = [1,2,4,6,8,0,-1]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(8,8)
# print(l1)
# l1.pop(4)
# print(l1.pop(3))

# list = [] and tuple = ()

# a = ("HArry", 4445,4646,False,True)
# print(a)
# no = a.count(4445)
# print(no)
#
# i = a.index(False)
# print(i)

# Practice set
# fruits = []
# f1 = input("Enter fruit name:")
# fruits.append(f1)
# f2 = input("Enter fruit name:")
# fruits.append(f2)
# f3 = input("Enter fruit name:")
# fruits.append(f3)
# f4 = input("Enter fruit name:")
# fruits.append(f4)
# f5 = input("Enter fruit name:")
# fruits.append(f5)
# print(fruits)

# marks = []
# m1 = int(input("Enter marks: "))
# marks.append(m1)
# m2 = int(input("Enter marks: "))
# marks.append(m2)
# m3 = int(input("Enter marks: "))
# marks.append(m3)
# m4 = int(input("Enter marks: "))
# marks.append(m4)
# m5 = int(input("Enter marks: "))
# marks.append(m5)
# marks.sort()
# print(marks)


#l =[1,22,444,5665]

# print(sum(l))


# a = (7,0,8,0,0,9)
# n = a.count(0)
# print(n)


#  Chapter 5 Dictionary and sets
# marks = {
#     "Harry": 100,
#     "Shubhan": 65
# }
# print(marks,  type(marks))
# print(marks["Harry"])

"""
unordered
mutable
indexed
can't be dup
"""

""" methods"""
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry": 99})
# print(marks)

# print(marks.get("Harry"))

"""Sets Methods"""
# s = {1,2,100,55,55}
# e = set()
# s.add(777)
# # print(s,type(s))
#
# print(len(s))
# s.remove(55)

# print(s)

# s1 = {1,2,3,54,6,8}
# s2 = {1,2,3,5,7,8,}
#
# print(s1.union(s2))
# print(s1.intersection(s2))

#  Chapter 5 practice sets
# H = {"apna":"Our",
#      "Bhai": "Brother",
#      "Pass": "pass",
#      "Hoga": "this"
#      }
# word = input("Enter The word you want: ")
# print(H[word])

#
# number = set()
# n = int(input("Enter a number: "))
# number.add(int(n))
# n = int(input("Enter a number: "))
# number.add(int(n))
# n = int(input("Enter a number: "))
# number.add(int(n))
# n = int(input("Enter a number: "))
# number.add(int(n))
# n = int(input("Enter a number: "))
# number.add(int(n))
# print(number)

# s = set()
# s.add(18)
# s.add("18")
# print(s)

# s = set()
# s.add(81)
# s.add(81.0)
# s.add("81")
# print(len(s))

# s = {}
# print(type(s))

# s = {}
# name = input("Enter your name : ")
# lang = input("Enter Your lang")
# s.update({name: lang})
# name = input("Enter your name : ")
# lang = input("Enter Your lang")
# s.update({name: lang})
# name = input("Enter your name : ")
# lang = input("Enter Your lang")
# s.update({name: lang})
# print(s)


# Conditional Expression
# a = int( input( "Enter your age: " ) )
#
# if (a >= 18):
#     print( "you are an adult" )
# elif (a <= 0):
#     print( "you are not even born and run the program again " )
# else:
#     print( "You are a minor" )

# import random
# pin = ""
# while len(pin) < 4:
#     digit = random.randint(0,9)
#     pin = pin + str(digit)
#
# print("Your pin is " + pin)

#
#
# letters = ["a", "b" ,"c"]
# for letter in enumerate(letters):
#     print(letter[0], letter[1])
#


# chapter 6 pracc tice set
# number1 = int(input("Enter a number :"))
# number2 = int(input("Enter a number :"))
# number3 = int(input("Enter a number :"))
# number4 = int(input("Enter a number :"))

# if (number1>number2 and number1>number3 and number1>number4):
#     print(f"This number is greater all which is {number1}")
# elif (number2>number1 and number2>number3 and number2>number4):
#     print(f"This number is greater all which is {number2}")
# elif (number3>number1 and number3>number2 and number3>number4):
#     print(f"This number is greater all which is {number3}")
# elif (number4>number1 and number4>number2 and number4>number3):
#     print(f"This number is greater all which is {number4}")


# marks1 = int(input("Enter a number :"))
# marks2 = int(input("Enter a number :"))
# marks3 = int(input("Enter a number :"))
# total_percentage = (100*(marks1 + marks2+ marks3))/300
# if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you pass " , total_percentage)
# else:
#     print("You failed ",total_percentage)

# p1 = "make a lot of money"
# p2 = "buy now "
# p3 = "subscribe this "
# p4 = "click this"


# msg = input("Enter a message:")
# if ((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#     print("This is a spam message")
# else:
#     print("This message is not a spam ")


"""loops"""


# for i in range( 1, 6 ):
# print(i)

# i = 0
# while(i<5):
#     print("*" *i)
#     i += 1

# i = 0
# while (i<5):
#     print("harry")
#     i +=1

# l = [1 , "harry",False,"JCU","Rohan"]
# i = 0
#
# while(i<len(l)):
#     print(l[i])
#     i +=1

# for i in range(4):
#     print(i)


# l = [1,22,44,5666,7777]
# for i in l:
#     print(i)
#
#
# t = (6,7,9,00,-1)
# for i in t :
#     print(i)


#loops practice
# n = int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{n} X {i} = {n * i} ")

# l = ["Mohit", "Rishan" , "yuvraj","Sohel","Sumit"]
#
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# n = int((inp

# n = int(input("enter a number "))
# i = 1
# sum = 0
# while (i <= n):
#     sum += i
#     i += 1
# print(sum)

# n = int(input("Enter a number: "))
# product = 1
# for i in range(1,n+1):
#     product = product * i
# print(f"The factorial of {n} is {product}")

# n = int(input("enter a number: "))
# for i in range(1 , n+1):
#     print(" " * (n- 1), end="")
#     print("*" * (2 * i-1),end="")
#     print("")
#
# n = int(input("enter a number"))
# for i in range (1,n+1):
#     print("*"* i , end=" ")
#     print(" ")

# n = int(input("Enter a number"))
# for i in range(1,n+1):
#     if(i==1 or i==n ):
#         print("*"* i,end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#     print("")


# chapter 8
# def avg():
#     a = int(input("Enter your number"))
#     b = int(input("Enter your number"))
#     c = int(input("Enter your number"))
#
#     average =(a+b+c)/3
#     print(average)
# avg()
# print("Thank you")

# def GoodDay():
#     name = input("Enter your name: ")
#     print(f"{name} have a Good Day")
#
#
# GoodDay()


# def GoodDay(name, ending):
#     print( "Good Day," + name )
#     print( ending )
#     return "ok"
#
#
# a = GoodDay( " mohit ", "Thanks" )
# print( a )

#
# def goodDay(name, ending="Thank you"):
#     print( f"Good Day, {name}" )
#     print( ending )
#
#
# goodDay( "Mohit", "thamks" )


#recurrsion
# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     return n * factorial( n - 1 )
#
#
# n = int( input( "Enter a number: " ) )
# print( f"The factorial of this number is:{factorial( n )}" )


#  praactice set
# def greatest(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif(b>c and b>a):
#         return b
#     elif (c>a and c>b):
#         return c
#
# a = 1
# b = 2
# c = 3
# print(greatest(a,b,c))


#
# def f_to_c(f):
#     return  5*(f-32)/9
#
# f = int(input("enter temperature in Fahrenheit: "))
# print(f"{f_to_c(f)}")


# oop
# class employee:
#     name = "harry"
#     language = " py"
#     salary = 120000
#
#
# harry = employee()
# print( harry.name, harry.language, harry.salary)
#

# class Employee:
#     language = "Python"
#     salary = 100000
#
# harry = Employee()
# harry.language = "java"
# print(harry.salary,harry.language)

#
# class Programmer:
#     company = "microsoft"
#
#     def __init__(self,name ,age ,salary):
#         self.name = name
#         self.age = age
#         self.salary=salary
#
# p = Programmer(name="hammy", age=22,salary=23000)
# print(p.name, p.age,p.salary)


# revision

# sports =["Ultra running","Cricket","baseball"]
# for i ,sports in enumerate(sports,start=1):
#     print(i,sports)

# word = "Dimaggio"
# for i ,letter in enumerate(word):
#     print(i,letter)

# team = ("rays", "man", "gay")
# for i,teams in enumerate(team):
#     print(i,teams)


