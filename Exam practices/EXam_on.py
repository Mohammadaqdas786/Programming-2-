# Write a Student class that inherits from Person (with name attribute).
# Add grade attribute and pass_course() method that prints "{name} passed!" if grade >= 50.
from string import digits

# p = Person("Alice")
# s = Student("Bob", 60)
# s.pass_course()  # Bob passed!
#

# class person:
#     def __int__(self, name):
#         self.name = name
#
#
# class student( person ):
#     def __init__(self, name, grade):
#         super().__init__( name )
#         self.grade = grade
#
#     def pass_course(self):
#         if self.grade >= 50:
#             print( f"The {self.name} has passed " )


# Given nums = [1, 2, 3, 4, 5], write code to print numbers from highest to lowest using slicing.

# Expected output: 5 4 3 2 1
# nums = [1, 2, 3, 4, 5]
# for num in nums[::-1]:
#     print(num, end=' ')
# # 5 4 3 2 1


# Write function get_high_calories(foods) that returns dict with only items where calories > 100.

# Example: get_high_calories({'apple': 50, 'cake': 400}) → {'cake': 400}

# def get_high_calories(food):
#     return [k: v for k , v in food.items() if v > 100]
#

# Given text = "hello123world456", extract only digits into a list [1,2,3,4,5,6].
# text = "hello123world456"
# digits = [int(char) for char in text if char.isdigit()]
# print(digits)

#
# class taxicab:
#
#     def __init__(self, fare_per_km):
#         self.fare_per_km = fare_per_km
#         self.odometer = 0
#
#     def get_fare(self):
#         return self.odometer * self.fare_per_km
#
#
# t = taxicab(2.5)
# t.odometer = 10
# print( t.get_fare() )

# class Taxicab:
#     def __init__(self, fare_per_km):
#         self.fare_per_km = fare_per_km
#         self.odometer = 0
#
#     def get_fare(self):
#         return self.odometer * self.fare_per_km
# t = Taxicab(2.5)
# t.odometer = 10
# print(t.get_fare())

#
# def make_menu(item, prices):
#     return {item: price for item, price in zip( item, prices )}
#
#
# print( make_menu( ['coffee', 'tea'], [3.5, 2.5] ) )

# numbers = [1,2,3,4,5,6,8,7,9]
# squares = [n**2 for n in numbers if n % 2 == 0]
# print(squares)

# name = 'Mohammad is here'
# print(' '.join(name.split()[::-1]))
# for i in range(1,5):
#     print( i * "*")

# class bank_account:
#     def __init__(self, balance=0):
#         self.balance =balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#     def withdraw(self,amount):
#         if 0 < amount <= self.balance:
#             self.balance -=amount
#         else:
#             print("invalid withdraw")


# def char_counter(text):
#     result = {}
#     for char in text.lower():
#         result[char] = result.get( char, 0 ) + 1
#     return result
#
#
# c = char_counter( "Mohammad" )
# print( c )

# nested = [[1,2], [3],[4,5,6]]
# flat = [item for sublist in nested for item in sublist]
# print(flat)

# class student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def passed(self):
#         return self.grade >= 50
#
#
# s = student( "mohammad", 65 )
# print( s.grade, s.name )

# numbers = [1,2,3,4,5,6,7,8,9]
# max_index = numbers.index(max(numbers))
# print(max_index)

#
# def unique_sorted(list):
#     return sorted(set(list))


# def triangle_area(length, breath):
#     return 0.5 * length * breath

# s = "hello world python"
# words_back = [word[::-1] for word in s.split()]
# print(' '.join(words_back))

# matrix = [[1,2,3], [4], [5,6,7]]
# row_sums = [sum(row)for row in matrix ]
# print(row_sums)

# class Employees:
#     def __int__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def give_raise(self, percent):
#         self.salary += (1 + percent / 100)


# sum numbers until 0 entered
# total = 0
# numbers = int(input("Enter a number: "))
# while numbers != 0:
#     total += numbers
#     numbers = int( input( "Enter a number: " ) )
# print(total)

# for loop sum
# def factorial(n):
#     result = 1
#     for i in range (1,n + 1):
#         result *= i
#     return result


# while countdown
# count = 5
# while count > 0:
#     print(count,end=' ')
#     count -= 1
#
# print("Blastoff!" )

# for i in range (1,31,3):
#     print(i , end=' ')

# total = 0
# count = 0
# number = int(input("Enter a number: "))
# while number != -1:
#     total += number
#     count += 1
#     number = int(input("Enter a number "))
# print(total/count)

# nested For pyramid
# for i in range(1,4):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# data = [3,7,2]
# for count in data:
#     print("*" * count,end=' ')

#
# def collatz_step(n):
#     steps = 0
#     while n != 1:
#         if n % 2 == 0:
#             n //=2
#         else:
#             n = n * 3 + 1
#         steps = 1
#     return steps
#
# n = 3
# for i in range(n):
#     print(' ' * i + 'X')

# def god(a,b):
#     while b != 0:
#         a,b = b, a % b
#     return a

# for i in range (1,3 ):
#     for j in range (i):
#         print(f"{i} X {j} ={i*j}", end='\t')
#     print()
#

# x = 5
# y = 10
# if x <10:
#     if y > 10 and x > 5:
#         print("A")
# else:
#     print("B")
