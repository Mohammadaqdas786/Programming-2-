# Write a program to input 2 numbers & print their sun
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# sum = a+b
# print(f"The sum of two number are: {sum}")


# WAP to input side of a square & print its area
# side_square = int(input("Enter a number for the side of square"))
# area = side_square * side_square
# print(f"The area of the square is {area}")

# WAP to input floating point numbers & print their average
# a = float(input("Enter a number "))
# b = float(input("Enter a number "))
# c = a+b/2
# print(f"The average of a & b is {c}")

# a = int(input("Enter a number "))
# b = int(input("Enter a number "))
#
# if a >= b:
#     print("True")
# else:
#     print("False")


# s = "This string has words in it"
# words = s.split()
# for i, word in enumerate( words ):
#     print( words[0:7] )
# """ 4
# 0 This
# 1 String
# 2 has
# 3 words
# 4 in
# 5 it
# """
#
# text = "I lOve PyThon"
# parts = text.upper().split()
# for i, word in enumerate( sorted( parts ) ):
#     print( len( word ), word, i )
#
# """ 4
# 1 I 0
# 4 LOVE 1
# 6 PYTHON 2
# """
#
# String = "I Love Python"
# print( String[::-1] )
#
# """ 4
# !nohtyP evoL I
# """

#
# def main():
#     for i in range(5):
#         do_thing=("*"* i)
#         print(do_thing(i))
# main()

# need more pratices
# for i in range(1, 4):
#     for j in range(2, 10, 3):
#         print(i, "-", j + i)
# """
# 2,5,8
# ---
# 4,15,11
# """
#  4
# numbers = [4, 10, 3, 25, 80]
# new_numbers = numbers
# c = numbers[:]
# print (numbers == c, numbers is new_numbers, numbers is c)


# def greet():
#     name = input( "Enter your name: " )
#     print( f"hello,{name}" )
#
#
# greet()


# def cube():
#     x = int ( input( "Enter a number: " ) )
#     print(f"The cube of {x} is {x**3}")
#
# cube()
# def convert_ceel_to_far():
#     temperature_in_celsius = float(input("Enter the temperature in Celsius: "))
#     temperature_in_far = temperature_in_celsius * 9/5 + 32
#     print( temperature_in_far )
# convert_ceel_to_far()


# def convert_far_in_cel():
#     temperature_in_far=float(input("Enetr temperature in Fahrenheit: "))
#     temperature_in_cel= (temperature_in_far-32)*5/9
#     print( temperature_in_cel )
# convert_far_in_cel()


""" 12
11,17,37
"""


# def greeting():
#     a = "HI"
#     print( a * 5 )
#
#
# greeting()


# def backward():
#     string = "I Love Python!"
#     print( string[::-1] )
#
#
# backward()'


# def main():
#     for i in range(5):
#         do_thing = ("*" * 2)
#         print(do_thing * i)
# main()


# def create_dictionary():
#     calories = [75 , 65 ,6175]
#     food = ["Egg", "Apple", "carrot cake "]
#     print(calories, food)
#
# create_dictionary()

#
# class Arbitrary(object):
#     def __init__(self, data=1):
#         self.data = data
#
#     def getit(self):
#         return self.data * 3
#
#
# class Thing(Arbitrary):
#     def __init__(self, value=6):
#         super().__init__(value * 8)
#
#
# a, b = Arbitrary(3), Thing()
# print(a.getit(), b.getit())
#
# """ output
# 9 , 48
#
# """

# name = input("Enter name")
# print(names)

# a = 0 <-10 or 100 != 100
# print(a)

# b = 2 + 265 % 2 > 89 -2**2
# print(b)


# class classroom:
#     def __inti__(self, room_name, maximum_occupancy):
#         self.room_name = room_name
#         self.maximum_occupancy = maximum_occupancy
#     def will_fit(self, number ):
#         return number <= self.maximum_occupancy
#
# b = classroom("A2-07", 35)
# result = b.will_fit(40)
#


# class plant:
#     def __init__(self, name, growth_rate):
#         self.name = name
#         self.growth_rate = growth_rate
#     def feed(self, amount_of_water):
#         self.amount_of_water = amount_of_water
#         height += self.amount_of_water * self.growth_rate
#
# b = plant(name="gave", growth_rate=20)
# print(b.name)
# print(b.growth_rate)



