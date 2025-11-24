# file i/o
# f = open("random.txt")
# data = f.read()
# print(data)
# f.close()

# st = "mohammad i m here"
# f = open("myfile.txt","w")
# f.write(st)
# f.close()

#OOP
#dry (donot repeat your self )

# class employee
# print( harry.salary, harry.language )

#Class Attribute :
#     language = "py"
#     salary = 120000
#
# #
# # harry = employee()
# class Employee:
#     language = "Python"
#     salary = 120000
#
#     def getinfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")
#
#
# Mohammad = Employee()
#
# Mohammad.getinfo()

# consturcter
# class Emyplotee:
#     language = "python"
#     salary = 1200000
#
#     def __init__(self, name, salary, language):
#         self.name = "Mohmmad"
#         self.salary = 130000
#         self.language = "java"
#
#         print( "i am mohammad " )
#
#     def getinfo(self):
#         print( f"The Language is {self.language}. The Salary is {self.salary}" )
#
#
# Mohammad = Emyplotee( "Mohammad", 130000, "java" )
# Mohammad.getinfo()


# inheretany


# class programmer:
#     Company = "ITC infotech"
#     def show(self):
#         print( f"Them name is {self.name} and The slary is {self.salary}" )
#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good  with {self.language()}")

# class employee:
#     Company = "ITC"
#
#     def show(self):
#         print( f"Them name is {self.Company} and The salary is ok" )
#
#
# class programmer( employee ):
#     Company = "ITC infotech"
#
#     def showlanguage(self):
#         print( f"The name is {self.Company} and he is good  with language" )
# a = employee()
# b = programmer()
# print(a.Company,b.Company)

# class Emplyee:
#     a =1
# class Programmer(Emplyee):
#     b =2
# class Manager(Programmer):
#     c = 3
# o = Emplyee()
# print(o.a)
# p = Programmer()
# print(p.b)
#
# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")
# e = Employee()
# e.a = 45
# e.show()



# def fun():
#     pass

