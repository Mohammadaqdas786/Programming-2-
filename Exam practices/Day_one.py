"""print("Hello World")
# Variable
age = 20
age = 30
price = 19.1909
first_name = 'Mohammad Aqdas Ayyub Lonbal'
Is_online = True
print(age)"""


# Practice 1
# Name = 'John Smith'
# age = 20
# is_new_patient = True

# Chapter_1
# print("Hello World")

# Chapter_2
# variable and data type
# a = 1
# b = 2
# print(a+b)

# a = 1  # a is an integer
# b = 5.22  # b is a floating point number
# c = "Mohammad"  # c  is a String
# d = False  # d is boolean
# e = None  # e is a none type variable

# # Arithmetic Operators
# a = 4
# b = 24
# c = b / a
# print( c )
#
# # Assignment Operators
# a = 4 - 2
# print( a )
# b = 6
# b += 3
# print( b )
#
# # Comparison Operators
#
# d = 5 > 4
# print( d )
#
# # logical Operator
#
# e = True or False
# print( e )
# # Truth table of or
# print( "True or False is ", True or False )
# print( "True or True is ", True or True )
# print( "False or True is ", False or True )
# print( "False or False is ", False or False )
#
# # Truth table of and
# print( "True and False is ", True and False )
# print( "True and True is ", True and True )
# print( "False and True is ", False and True )
# print( "False and False is ", False and False )
#
# # type function
# a = 31.2
# t = type( a )  # class <int>
#
# print( t )
#
# # input function
# a = int( input( "Enter a number: " ) )
# b = int( input( "Enter a number: " ) )
#
# print( "The sum of a + b is :", a + b )

# Chapter 3 :- Strings
# name = "Aqdas"
# name_short = len( name )
# charater1 = name[0:4]
# print( name_short, charater1 )
#
# word = "kingfisher "
# b = word[:7: 3]
# print(b)
#
# # Strings Function
# name = "fernado"
# print(len(name))
# print(name.endswith('ado'))
# print(name.startswith("fern"))
# print(name.capitalize())
#
# a = ('I am a good guy\nbut not a bad \n guy')
# print(a)

# Chapter 4 - list and tuples
# friends = ["Apple", "Orange", 5 , 345.06, False, "Aakash", "Rohan" ]
#
# friends[0]= "Grapes"
# print(friends[0:-1:2])
# print(friends[1])
# print(friends[2])
# print(friends[3])

# # List_methods
# friends = ["Apple", "Orange", 5 , 345.06, False, "Aa kash", "Rohan" ]
# print(friends)
#
# friends.append("Mohammad")
# print(friends)
#
# l1 = [1,2,3,5,6,4,7,8,9,0]
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(1,22222)
# print(l1)
# l1.pop(8)
# print(l1.pop(8))
# l1.remove(6)
# print(l1.remove(8))

# Tuple
# a = (1,100,200,234,False,"Mohammad", 'Vanya')
# print(type(a))
#
# no = a.count(100)
# print(no)
#
# i = a.index(100)
# print(i)

# Dictionary & Sets
# marks = {
#     "mohammad": 50,
#     "rahul": 40,
#     "Vishik": 45,
# }
# print( marks, type( marks ) )

# Dic methods
# marks = {
#     "kane": 20,
#     "dean": 39,
#     "elsa": 29,
#     "petr": 0,
# }
# print( marks.items() )
# print(marks.keys())
# # print(marks,values())
# marks.update({"petr":50})
# print(marks)

# Sets

# e = set()
# s = {1,5,5,5,32,64}
# print(s)

# Sets methods
# s = {1,5,5,5,32,64,True}
# print(s)
#
# s.add(666)
# print(s)

# Set union
# s1 = {1, 2, 56, 9}
# s2 = {7, 8, 9, 0}
# print( s1.union( s2 ) )
# print( s1.intersection( s2 ) )
#


# conditonal expression

# a = int( input( "enter your age" ) )
# if a >= 18:
#     print( "you are old" )
# elif a<0:
#     print("invaild age ")
# else:
#     print( "you are under age " )

# age = int( input( "Enter your Age: " ) )
#
# if age % 2 == 0:
#     print( "a is even " )
# if age > 18:
#     print( "you are above the age of consent " )
#     print( "good for you" )
# elif age < 0:
#     print( "you are entering an invaild negative age " )
# else:
#     print( "you are below the age of comsent " )
# print( "end of program" )

# LoOps
# for i in range( 1, 6 ):
#     print( i )
#
# while(i<6):
#     print(i)
# #     i +=1
#
#
# I = [1, 2, "mo", "va", False]
# i = 0
# while (i < len( I ) + 1):
#     print( I[i] )
#     i += 1
#
# for i in range(4):
#     print(i)

# l = [1,2,45,6,7,9,]
#
# for i in l :
#     print(i)
#
# s = "mohammad"
# for i in s :
#     print(i)

# L =[1,2,3,4,5,6,]
#
# for item in L :
#     print(item)
# else:
#     print("done")

# for i in range(100):
#     if (i == 34 ):
#         continue
#     print(i)
#
# for i in range( 645 ):
#     pass
#
# i = 0
# while (i < 45):
#     print( i )
#     i +=1

# Chapter 8
# def avg():
#     a = int( input( "Enter your Number " ) )
#     b = int( input( "Enter your Number " ) )
#     c = int( input( "Enter your Number " ) )
#
#     average = (a + b + c) / 3
#     print( average )
#
#
# avg()
# print( "Thank u" )

#
# def greet():
#     name = input( "Enter your Name " )
#     print( f"Good Morning {name}" )
#
#
# greet()
#
# def GoodDay(name,ending):
#     print("Good Day "+ name)
#     print(ending)
#
#
# GoodDay("Mohammad", "Thank u")

# def GoodDay(name,ending ="Thank You"):
#     print(f"Good Day {name}")
#     print(ending)
#
#
# GoodDay("Mohammad")

# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     return n * factorial( n - 1 )
#
#
# n = int( input( "Enter a number:" ) )
# print( f"The Factorial of this number is: {factorial( n )} " )
