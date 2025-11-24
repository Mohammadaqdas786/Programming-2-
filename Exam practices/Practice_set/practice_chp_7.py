# problem 1
from docutils.io import Input

# n = int(input("Enter a Number "))
#
# for i in range(1,11):
#     print(f"{n} X {i}= {n * i}")

# problem 2
# l = ["vanya", "vansa", "venika","Sohal"]
# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

# Problem 3
# n = int( input( "Enter a Number " ) )
# i = 1
#
# while (i < 11):
#     print( f"{n} X {i}= {n * i}" )
#     i += 1

# n = int(input("Enter a Number "))
#
# for i in range(2,n):
#     if (n%i) == 0:
#         print("Number is not prime ")
#         break
# else:
#     print("Number is Prime ")

# n = int(input("Enter a Number "))
# i = 1
# sum = 0
# # while(i<n):
#     sum += i
#     i+=1
# print(sum)

# n = int(input("Enter a Number "))
# product =1
# for i in range (1, n+1):
#     product = product * i
# print(f"The Factorial of {n} is {product}")

#problem 7
# n = int( input( "Enter the number " ) )
# for i in range( 1, n + 1 ):
#     print( "*" * (n - i),end="")
#     print( "*" * (2*i-1), end="" )
#     print("\n")

# n = int( input( "Enter a number " ) )
# for i in range( 1, n + 1 ):
#     if (i == 1 or i == n):
#         print( "*" * n ,end="")
#     else:
#         print( "*", end="" )
#         print( " " * (n - 2), end="" )
#         print( "*", end="" )
#     print( "" )

n = int( input( "Enter a number " ) )
for i in range(1,11):
    print(f"{n} X {11-i}={n*(11-i)}")