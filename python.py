import time
from functools import reduce
import os
# print('Hello World!' * 2)
# print('''
# Hi Kartikey,
# Welcome to Python Course!
# ''')

# def greet(firstname,middlename,lastname="Kumar"):
#     print(f"Hi {firstname} {lastname}")

# greet('Kartikey',lastname='Goel',middlename='Kumar')

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getAge(self):
#         return self.age

#     def getName(self):
#         return self.name


# person1 = Person('Kartikey', '25')
# print(person1.name)

# import module2 as m2
# from sum import sum

# result = sum(1, 2)
# print(result)

# pakages
# from calculations.calc import sum
# from calculations import *

# print(calc.__doc__)
# result = sum(1, 2)
# print(result)

# working with paths
# from pathlib import Path

# 2 types - absolute and relative paths
# path = Path("Random")
# path.mkdir()
# path.rmdir()

# path = Path()
# for file in path.glob('*.py'):
#     print(file)

# import openpyxl as xl
# from openpyxl.chart import Reference, BarChart
# wb = xl.load_workbook('price.xlsx')
# # print(dir(wb['Sheet1']['a1']))
# # print(wb['Sheet1']['A1'].value)
# # print(wb['Sheet1'].max_row)

# for row in range(2, wb['Sheet1'].max_row+1):
#     # for column in range(wb['Sheet1'].max_column):
#     # print(chr(ord('a')+column)+str(row))
#     # cell = wb.get_sheet_by_name('Sheet1').__getitem__(
#     #     chr(ord('a')+column)+str(row))
#     # cell = wb['Sheet1'][str(str(ord('a')+column)+str(row))]
#     # print(dir(cell))
#     # product = wb['Sheet1']['A'+str(row)].value
#     # price = wb['Sheet1']['B'+str(row)].value
#     # print(product,'|',price)
#     original_price = wb['Sheet1'].cell(row, 2).value
#     updated_price = original_price * 1.1
#     wb['Sheet1'].cell(row, 3).value = updated_price

# values = Reference(wb['Sheet1'], min_row=2, max_row=11, min_col=3, max_col=3)
# chart = BarChart()
# chart.add_data(values)
# wb['Sheet1'].add_chart(chart=chart, anchor='D2')

# wb.save('updated_price_table.xlsx')

# doc strings


# def square(x):
#     ''' This function squares a number '''
#     return x**2


# print(square.__doc__)

# recursion

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# sets

# s = {} # this creates empty dictionary
# s = set() # this creates empty set
# s = {1, 2, 1, 1, 1, 2, 3, 4, 4, 5, 5}
# print(s)

# We can use else with for loops and while loops, it will always execute if loops finishes successfully,
# but if break statememt is used it does not execute

# virtual environment
# pip freeze  --- gives all modules and packages installed in the virtual Environment

# if __name__ == "__main__"  --->  used in modules

# os module
# import os
# os.rmdir('OS')

# global and  local variables
# x = 4


# def changeVariable():
#     global x
#     x = 5
#     print(x)


# print(x)

# file IO
# import time
# from functools import reduce
# import os
# print(os.getcwd())
# os.chdir('calculations')
# print(os.getcwd())
# list = os.listdir()
# for file in list:
#     if file.endswith('.py'):
#         print(file)

# print(os.path.dirname())
# f = open('requirements.txt','rb')
# text = f.read()
# print(text)
# f.close()

# writing a file
# with open('first.txt', 'w') as file:
#     # file.write('Hi I am Kartikey Goel.\nI am a software engineer')
#     file.write('''Hi Hello, we are using writelines
# Hi Hello, we are using writelines
# Hi Hello, we are using writelines
# ''')

# reading a file
# with open('first.txt','r') as file:
#     print(file.readlines())

# seek tell
# with open('first.txt', 'w') as file:
#     # file.seek(5)
#     # print(file.tell())
#     # r = file.read(5)
#     # print(file.tell())
#     # print(file.read(5))
#     file.write('Hi I am a python developer')
#     file.truncate(50)

# lamba functions

# sum = lambda x,y: x+y

# print(sum(1,2))

# map filter and reduce


# def double1(n):
#     return n * 2


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square_list = map(double1, l)


# print(list(square_list))

l = [1, 2, 3, 4, 5]

# map
# print(list(map(lambda x: x*2, l)))

# filter
# print(list(filter(lambda x: x % 2 == 0, l)))


# reduce
# print(reduce(lambda x, y: x+y, l))

# is vs == comparison operators

# is --- this looks for exacts match between memory location of object
# == -- this compares only values

# args and kwargs

# def sum(*args,**kwargs):
#     print(kwargs)
#     return 1


# print(sum(1,2,3,a=1,b=2,c=3))

# decorators


# def decor(fn):

#     def timecalc(*args, **kwargs):
#         start = time.time()
#         res = fn(*args)
#         end = time.time()
#         print("Total time taken by functions is: ", end-start)
#         return res

#     return timecalc


# @decor
# def sum(a, b):
#     time.sleep(2)
#     return a+b


# print(sum(2, 3))

# @property decorator
# https://www.freecodecamp.org/news/python-property-decorator/


# class House:
#     def __init__(self, price):
#         self.__price = price
#         # self.__price = price # We can access this by _House__price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if isinstance(value, float) and value > 0:
#             self.__price = value

#     @price.deleter
#     def price(self):
#         del self.__price


# house1 = House(10)
# # print(dir(house1))
# print(house1.price)

# @staticmethod
# static methods # doesn't depend on class instance, can be called directly using class, no need to add self keyword
# Instance methods are methods that are bound to an instance of a class, and have access to the instance and its attributes.
# Static methods, on the other hand, are not bound to an instance and do not have access to the instance or its attributes.
# class Math:
#     def __init__(self, num):
#         self.num = num

#     @staticmethod
#     def add(x, y):
#         return x+y


# print(Math.add(2,3))
# print(Math(10).add(2, 3))

# Instance vs class variables
# code will look for instance variables first then class variables

# class Employee:
#     companyName = 'Microsoft'

#     def showCompanyName(self):
#         return f"The company name is {self.companyName}"


# emp1 = Employee()
# # emp1.companyName = 'Apple'
# print(emp1.showCompanyName())

# os.chdir(os.path.join(os.getcwd(), 'files'))
# for file in range(26):
#     os.makedirs(f"file{chr(ord('a') + file)}")
#     os.rmdir(f"file{chr(ord('A') + file)}")

# dir = os.listdir()
# for index, file in enumerate(dir):
#     os.rename(file, f"{file[0:-1]}{index}")

# diff bw mkdir and makedirs is makedirs also creates intermediate directories present in path specified whereas mkdir
# does not create intermediate directories

# class method

# A class method is a method that is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that would be applicable to all instances.

# class Person:

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# person1 = Person()
# person1.changeName('Kartikey')
# print(person1.name)
# print(Person.name)

# using classmethod as constructor


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromstr(cls, str1):
#         return cls(str1.split("-")[0], str1.split("-")[1])

#     def getNameandAge(self, str1):
#         return c

#     def getName(self):
#         return self.name


# str1 = "Kartikey-25"
# # p1 = Person("Kartikey", 25)

# # print(p1.getNameandAge(str1))
# person1 = Person.fromstr(str1)
# print(person1.name)
# print(person1.age)

# dict = {
#     "name": "Kartikey",
#     "age": 25
# }

# print(dir(dict))

# super keyword

# when a child class inherits a method from parent class, it can override the parent method, but in some cases we want to call
# the parent method, so we use the super keyword

# class Parent:
#     def parentMethod(self):
#         print("this is a parent method")


# class Child(Parent):
#     def childMethod(self):
#         print("this is a child method")

#     def parentMethod(self):
#         print("added some modifications in child parent method")
#         super().parentMethod()


# child1 = Child()
# child1.parentMethod()

# dunder/magic methods
# https://www.geeksforgeeks.org/dunder-magic-methods-python/

# operator overloading

# multiple inheritance

# class Father:
#     bank_balance = "xxxxx"

#     def __init__(self, name):
#         print("Father class is invoked")
#         self.name = name

# class Mother:

#     jewellery = "100gm"

#     def __init__(self, name):
#         print("Mother class is invoked")
#         self.name = name


# class Child(Father, Mother):
#     def __init__(self, name):
#         print("Child class is invoked")
#         self.name = name


# c1 = Child("Kartikey")
# print(c1.bank_balance)
# print(c1.jewellery)
