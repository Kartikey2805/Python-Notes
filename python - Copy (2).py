import time
from functools import reduce
import os

# https://www.codewithharry.com/blogpost/python-cheatsheet/

# print('Hello World!' * 2)
# print('''
# Hi Kartikey,
# Welcome to Python Course!
# ''')

# a // b (does integer division) like 4 // 3 gives 1 not 1.33333
# a ** 2 # squares a number 

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
# from module1 import sum

# def sum(*args,**kwargs):
#     # args is tuple
#     # kwargs is dictionary
#     print(args)
#     print(kwargs)
#     print(args[0])
#     s = 0
#     for n in args:
#             s += n
#     return s

# print(sum(1,2,3,4,key="sum"))

# result = sum(1, 2)
# print(result)

# modules
# https://realpython.com/python-modules-packages/

# Reloading a Module
# If you make a change to a module and need to reload it,
# you need to either restart the interpreter or use a function called reload() from module importlib:

# pakages
# from calculations.calc import sum
# from calculations import calc
# print(calc.__name__)

# Note that this does not make the module contents directly accessible to the caller. 
# Each module has its own private symbol table, which serves as the global symbol table for all objects defined in the module.
# Thus, a module creates a separate namespace, as already noted.

# namespaces - The namespaces in Python is a container that holds identifiers (names of variables, functions, classes, etc.) and maps them to their corresponding objects. It acts as a boundary, ensuring that names are unique and avoiding naming conflicts. Python provides multiple types of namespaces
# The built-in function dir() returns a list of defined names in a namespace. 
# Without arguments, it produces an alphabetically sorted list of names in the current local symbol table:

# calc.privateVar = "Not Private"
# print(calc.privateVar)
# print(calc.__doc__)
# result = sum(1, 2)
# print(result)

# working with paths

# https://realpython.com/python-pathlib/

# Working with files and interacting with the file system are common tasks for Python developers. 
# Some cases may involve only reading or writing files, but sometimes more complex tasks are at hand.
# Maybe you need to list all files of a given type in a directory, find the parent directory of a given file,
# or create a unique filename that doesn’t already exist. That’s where pathlib comes in.

from pathlib import Path
# for filePath in Path.cwd().glob('*.cpp'):
#     print(filePath)
#     Path.mkdir('Archive')
#     newPath = Path(f'Archive/{filePath.name}')
#     print(newPath.exists())
#     filePath.replace(newPath)
    # Path.replace(filePath,newPath)

# >>> from pathlib import Path
# >>> path = Path(r"C:\Users\gahjelle\realpython\test.md")
# >>> path
# WindowsPath('C:/Users/gahjelle/realpython/test.md')

# >>> path.name
# 'test.md'

# >>> path.stem
# 'test'

# >>> path.suffix
# '.md'

# >>> path.anchor
# 'C:\\'

# >>> path.parent
# WindowsPath('C:/Users/gahjelle/realpython")

# >>> path.parent.parent
# WindowsPath('C:/Users/gahjelle')

# Path.home()

# create new file 
# Path.touch('new.txt')

# 2 types - absolute and relative paths
# path = Path("Random")
# path.mkdir()
# path.rmdir()

# path = Path()
# for file in path.glob('*.py'):
#     print(file)

# copy a file 

# from pathlib import Path
# import shutil

# # Source file path
# source_file = Path("path/to/source/file.txt")

# # Destination folder path
# destination_folder = Path("path/to/destination/folder")

# # Copy the file to the destination folder
# shutil.copy(source_file, destination_folder)

# other way to copy without shutil 

# from pathlib import Path

# # Source file path
# source_file = Path("path/to/source/file.txt")

# # Destination folder path
# destination_folder = Path("path/to/destination/folder")

# # Read the content of the source file
# with open(source_file, "rb") as f:
#     file_content = f.read()

# # Destination file path
# destination_file = destination_folder / source_file.name

# # Write the content to the destination file
# with open(destination_file, "wb") as f:
#     f.write(file_content)


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
# print(type(factorial))

# sets

# s = {} # this creates empty dictionary
# s = set() # this creates empty set
# s = {1, 2, 1, 1, 1, 2, 3, 4, 4, 5, 5}
# print(type(s))
# print(s)

# We can use else with for loops and while loops, it will always execute if loops finishes successfully,
# but if break statememt is used it does not execute

# virtual environment
# pip freeze  --- gives all modules and packages installed in the virtual Environment

# if __name__ == "__main__"  --->  used in modules

# # os module

# import os
# print(os.name)
# # print((os.environ))
# print(os.getenv('HOME','display this if the variable is not present'))
# # os.rmdir('OS')
# cwd = os.getcwd()

# # List the details
# for dirpath, dirnames, filenames in os.walk(cwd):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)

# global and  local variables
# x = 4


# def changeVariable():
#     global x
#     x = 5
#     print(x)

# changeVariable()
# print(x)

# file IO
# import time
# from functools import reduce


# import os

# https://www.w3resource.com/python-exercises/os/index.php

# print(os.getcwd())
# os.chdir('calculations')
# print(os.getcwd())

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

# x = 'NULL';

# with open('first.txt','r') as file:
#     # print(file.readlines())
#     x = file.read()

# print(x)

# seek tell
# with open('first.txt', 'r') as file:
#     file.seek(5)
#     print(file.tell())
#     r = file.read(5)
#     print(file.tell())
#     print(file.read(5))
    # file.write('Hi I am a python developer')
    # file.truncate(50)
    # print(file.tell())


# lamba functions

# sum = lambda x,y: x+y

# print(sum(1,2))

# map filter and reduce


# def double1(n):
#     return n * 2


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square_list = map(double1, l)


# print(list(square_list))

# l = [1, 2, 3, 4, 5]

# map
# print(list(map(lambda x: x*2, l)))

# filter
# print(list(filter(lambda x: x % 2 == 0, l)))

# from functools import reduce

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
# https://www.geeksforgeeks.org/decorators-in-python/

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
# print(Employee.companyName)

# os.chdir(os.path.join(os.getcwd(), 'files'))
# for file in range(26):
#     os.makedirs(f"file{chr(ord('a') + file)}")
#     os.rmdir(f"file{chr(ord('A') + file)}")

# dir = os.listdir()
# for index, file in enumerate(dir):
#     os.rename(file, f"{file[0:-1]}{index}")

# diff bw mkdir and makedirs is makedirs also creates intermediate directories present in path specified whereas mkdir
# does not create intermediate directories

# https://realpython.com/instance-class-and-static-methods-demystified/

# class method

# A class method is a method that is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. 
# For example, it can modify a class variable that would be applicable to all instances.

# class Person:

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# person1 = Person()
# person1.changeName('Kartikey')
# print(person1.name)
# person2 = Person()
# print(person2.name)
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


# class Welcome:
#     def greet(self):
#         print('Welcome!')

# print(Welcome.greet())        
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

# print(dir(int)) 

# class Student:
#     def __init__(self,name):
#         self.name = name


# operator overloading

# multiple inheritance

# class Father:
#     bank_balance = "xxxxx"
#     print('Father class is invoked')
#     def __init__(self, name):
#         print("Father class is invoked")
#         self.name = name

# class Mother:
#     jewellery = "100gm"
#     print("Mother class is invoked")
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

# time module 
# import time
# print(time.time())
# print(time.localtime())
# t = time.localtime()
# formatted_time = time.strftime('%Y-%m-%d %H:%M:%S',t)
# print(formatted_time)
# time.sleep(4)
# print('this will execute after 4 seconds')

# str = "hello"

# for i in enumerate(str):
#     print(i)  
#     print(len(i))  

# l = [('W',5),('E',2)]
# for i in l:
#     print(i[0])

# class CustomException(Exception):
#     errorcode = None
#     def __init__(self):
#         print('Base Exception is executed')
#         super().__init__('This is customer error with error code {0}'.format(self.errorcode))

# class Errorclass1(CustomException):
#     errorcode = '409'

# raise Errorclass1()

# In below case __init__ method of Parent will execute as child does not have a __init__ method, __init__ is always looked
# from bottom to up until found in one class 

# class Parent:
#     def __init__(self,name):
#         print('parent')
#         self.name = name

# class Child(Parent):
#     # def __init__(self, name):
#     #     self.name = name
#     name = 'Child'

# c = Child()

# MultiThreading

# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.
# In Python, we can use the threading module to implement multithreading.

# import threading
# import time 

# res = []

# def func(seconds):
#     print(f"this work will take around {seconds} seconds")
#     time.sleep(seconds)
#     return f"time taken {seconds} seconds"
#     # val = f"time taken {seconds} seconds"
#     # res.append(val)

# # thread initialization 
# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])

# # starting a thread 
# t1.start()
# t2.start()

# # waiting for thread to complete before going to other code after this
# t1.join()
# t2.join()

# # both threads will complete in 4 seconds 
# print(res)

# for storing results 
# from concurrent.futures import ThreadPoolExecutor

# list = [4,2,1]
# res = []
# with ThreadPoolExecutor() as executor:
#     res = executor.map(func,list)

# for ele in res:
#     print(ele)

# MultiProcessing 

# import multiprocessing
# import concurrent.futures
# import requests

# def downloadFile(url, name):
#   print(f"Started Downloading {name}")
#   response = requests.get(url)
#   open(f"files/file{name}.jpg", "wb").write(response.content)
#   print(f"Finished Downloading {name}")
 


# url = "https://picsum.photos/2000/3000"
# # pros = []
# # for i in range(50):
# #   # downloadFile(url, i)
# #   p = multiprocessing.Process(target=downloadFile, args=[url, i])
# #   p.start()
# #   pros.append(p)

# # for p in pros:
# #   p.join()

# with concurrent.futures.ProcessPoolExecutor() as executor:
#   l1 = [url for i in range(60)]
#   l2 = [i for i in range(60)]
#   results = executor.map(downloadFile, l1, l2)
#   for r in results:
#     print(r)

# json module 
# https://www.w3schools.com/python/python_json.asp

import json

# path = Path.joinpath(Path.cwd(),'file.json')

# with open(path,'r') as file:
    # f = json.load(file)
    # print(f["name"])
    # print(f["age"])
    # print(file.read()) # this cannot parse json like above

# print(f)

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	    String
# int	    Number
# float	Number
# True	true
# False	false
# None	null


# Convert a Python object containing all the legal data types:

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))

# indentation 
# print(json.dumps(x, indent=2))

# seperators 
# print(json.dumps(x, indent=4, separators=(". ", " = ")))


# sort keys 
# print(json.dumps(x, indent=4, sort_keys=True))

# csv module 

# import csv

# # Open the CSV file for reading
# with open('employees.csv', mode='r') as file:
# 	# Create a CSV reader with DictReader
# 	csv_reader = csv.DictReader(file)

# 	# Initialize an empty list to store the dictionaries
# 	data_list = []

# 	# Iterate through each row in the CSV file
# 	for row in csv_reader:
# 		# Append each row (as a dictionary) to the list
# 		data_list.append(row)

# # Print the list of dictionaries
# for data in data_list:
# 	print(data)

# # importing the csv module
# import csv
# # field names
# fields = ['Name', 'Branch', 'Year', 'CGPA']
# # data rows of csv file
# rows = [['Nikhil', 'COE', '2', '9.0'],
# 		['Sanchit', 'COE', '2', '9.1'],
# 		['Aditya', 'IT', '2', '9.3'],
# 		['Sagar', 'SE', '1', '9.5'],
# 		['Prateek', 'MCE', '3', '7.8'],
# 		['Sahil', 'EP', '2', '9.1']]
# # name of csv file
# filename = "university_records.csv"
# # writing to csv file
# with open(filename, 'w') as csvfile:
# 	# creating a csv writer object
# 	csvwriter = csv.writer(csvfile)
# 	# writing the fields
# 	csvwriter.writerow(fields)
# 	# writing the data rows
# 	csvwriter.writerows(rows)

# import csv

# with open('t.txt') as file:
#     print(file.read())
#     f = csv.reader(file)
#     for data in f:
#         print(data[0])

# command line arguments 
# from argparse import ArgumentParser
# parse = ArgumentParser()
# parse.add_argument('arg1',type=int)
# parse.add_argument('arg2',type=str)
# args = parse.parse_args()
# print(args.arg1)
# print(args.arg2)



# # octal to decimal using int()
# print("int() on 0o12 =", int('0o12', 8))
 
# # binary to decimal using int()
# print("int() on 0b110 =", int('0b110', 2))
 
# # hexa-decimal to decimal using int()
# print("int() on 0x1A =", int('0x1A', 16))

# format 
# 56.0 to 56.00
# n = 56.0 
# format(n,'.2f')

# math module 
# import math


# re module (regular exp)

# Regular expressions are a powerful tool for matching patterns within text. They’re used for searching, replacing, and parsing strings based on specific patterns. Here’s a quick overview of some basic regex components:

# Literals: These are the simplest form of pattern matching. For example, a will match any occurrence of the character ‘a’.
# Character Classes: These are used to match any one of a specific set of characters. For example, [abc] will match any single ‘a’, ‘b’, or ‘c’.
# Dot (.): This special character matches any single character except newline characters. For example, a.b will match ‘acb’, ‘aab’, ‘a3b’, etc.
# Anchors: These specify the start and end of a string. ^ denotes the start, and $ denotes the end. For example, ^a will match any string that starts with ‘a’.
# Quantifiers: These specify how many instances of a character or group must be present for a match.
# * matches zero or more times.
# + matches one or more times.
# ? matches zero or one time.
# {n} matches exactly n times.
# {n,} matches at least n times.
# {n,m} matches between n and m times.
# Groups and Ranges:
# Parentheses () are used to define groups.
# A vertical bar | denotes an “or” condition.
# A hyphen - within square brackets denotes a range of characters.
# Escape Character: The backslash \ is used to escape special characters.
# Here’s an example of a regex pattern and its explanation:

# ^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$

# This pattern matches email addresses:

# ^ and $ anchor the pattern to match the entire string.
# ([a-z0-9_\.-]+) matches the username part of the email, which can contain lowercase letters, numbers, underscores, periods, and hyphens.
# @ is a literal character that appears in all email addresses.
# ([\da-z\.-]+) matches the domain part, which can contain letters, numbers, periods, and hyphens.
# \. matches the literal dot.
# ([a-z\.]{2,6}) matches the top-level domain, which can be between 2 to 6 letters long.

# import re

# n  = int(input('Enter no of testcases: '))

# for _ in range(n):
#     s = input('Enter a regex: ')
#     try:
#         print(bool(re.compile(s)))
#         # print(True)
#     except:
#         print(False)


# string  = 'aababab'
# regex = 'a(ab){3}'

# if re.match(string=string,pattern=regex):
#     print('Yes the string matched with regex')
# else:
#     print('The string didn\'t match with regex')


# strings 

# s = "kartikey goel"
# s = s.lower()
# l = s.split(' ')
# l = [name.capitalize() for name in l]
# s = ' '.join(l)


# The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.

# For example:

# >>> eval("9 + 5")
# 14
# >>> x = 2
# >>> eval("x + 3")
# 5

# any() This expression returns True if any element of the iterable is true.
# all() This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.


# l = input().split()
# print(l)


# Numpy 
# import numpy as np 
# print(np.array([1,2,3,4,5]))

# Fixed Memory Allocation: When you create a list in some programming languages, you have to specify the size upfront. For example, in C or C++, you might declare an array with a fixed size like int myArray[10];. This means the array can hold exactly 10 elements, and it won't change unless you explicitly resize it.
# Dynamic Memory Allocation: In Python, lists are dynamic, meaning they can grow or shrink as needed. You don't need to specify the size upfront. When you create a list, Python allocates a small chunk of memory to hold some initial elements.
# Flexible Growth: As you add elements to the list, Python keeps track of how full the current memory allocation is. When the list becomes too full, Python automatically allocates a larger chunk of memory, typically doubling the previous capacity. It then copies the existing elements to the new memory location and adds the new element.
# Automatic Memory Management: Python handles all of this memory management for you behind the scenes. You don't need to worry about resizing arrays or deallocating memory when you're done with a list. Python's garbage collector takes care of cleaning up unused memory.
# So, in essence, Python lists don't have a fixed size or fixed memory allocation. They can grow or shrink dynamically as you add or remove elements, making them very convenient to use.

# used for multi D Arrays 
# every element should be of same type 

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     # used to find length
#     def __len__(self):
#         return len(self.name)
    
#     # used for return value when obj is created
#     def __repr__(self):
#         print('repr is called')
#         return str({
#             "name":self.name,
#             "age":self.age
#         })
    
#     # used for print(), takes priority over repr when both are defined
#     def __str__(self):
#         return "Object created successfully"
    
#     # equality check, we can implement for __ne__ (not equal), __lt__ (less than)
#     def __eq__(self,other):
#         if self.name == other.name and self.age == other.age:
#             return True
#         else:
#             return False


# s1 = Student('Kartikey',24)
# s2 = Student('Kartikey',24)

# print(s1) # __repr__ is used if __str__ is not defined
# print(s1)  # __str__ is used when both __str__ and __repr__ are defined
# print(len(s1)) # __len__ is used
# print(s1 == s2) # __eq__ is used

# print('some value',end='\t') # we can use end

# list insert 

# l = [1,2,3,4,4]
# index, value = [1,5]
# l.insert(index,value)
# print(l)

# remove
# l.remove(4)
# print(l)

# consecutive elements 
# from itertools import groupby

# s = input()

# for key, group in groupby(s, lambda x: x):
#     print(key)
#     print(list(group))


# for key, group in groupby(s, lambda x: x):
#     print(key,len(list(group)))

# dict = {'Key1':10,'key3':8,'key2': 5}

# print(dict.items())

# for x in dict.items():
#     print(type(x))
#     print(x[0])

# l = list(dict)

# my_dict = {'apple': 3, 'banana': 2, 'orange': 3, 'pear': 2}

# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[1], x[0]),reverse=True))

# print(sorted_dict)

# sets 

# myset = {1, 2}
# myset.add('c')
# myset.update([1, 2, 3, 4]) # update() only works for iterable objects

# Both the discard() and remove() functions take a single value as an argument and removes that value from the set. 
# If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.

# COMMON SET OPERATIONS Using union(), intersection() and difference() functions.

# s = {12,4,38}
# ns = sorted(s)
# print(type(ns))
# for x in ns:
#     print(x)

# a = {1,2,3,4,5,6,7,8}
# b = {4,5,6,7,8,9,10}

# # print(a.difference(b))
# print(a.intersection(b))
# print(a.union(b))

# s = 'abcd'

# def message(transaction):
#     def wrapper(*args):
#         transaction(args[0])
#         print('Transaction is successfull')
#     return wrapper

# @message
# def transaction(amount):
#     print(f'transaction initiated, account will be debited with {amount}')

# print(transaction(100))

# from functools import reduce

# s = 'abcd'
# ans = reduce(lambda x, y : (x or y.isalnum()), s, False)
# print(ans)

# from itertools import permutations, combinations
# l = [1,2,3]
# s = "HACK"
# print(str(permutations(s,2)))
# print(list(permutations(l,2)))
# print(list(combinations(l, 2)))

# regex 
# import re
# # https://www.geeksforgeeks.org/regular-expression-python-examples/ 
# n = int(input())
# credit_cards = []

# for _ in range(n):
#     credit_cards.append(input())

# pattern = r'^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'

# for s in credit_cards:
#     print(re.findall(pattern, s))

# command line arguments 
# import sys

# args = sys.argv

# print(args[1], args[2])

# The walrus operator (:=) was introduced in Python 3.8 and allows you to assign values to variables as part of an expression. 
# This can make certain operations more concise and potentially more readable. 
# Here are a few examples to illustrate its use:

# Without the walrus operator:

# data = input("Enter some data: ")
# while data != "quit":
#     print(f"You entered: {data}")
#     data = input("Enter some data: ")

# With the walrus operator:

# while (data := input("Enter some data: ")) != "quit":
#     print(f"You entered: {data}")


import shutil # used for high level file operations
# shutil.copy('python.py','pythonCopy.py') #c only used to copy files
# shutil.copytree('calculations','calculationsCopy') # used to copy entire directory and its content
# shutil.rmtree('calculationsCopy') # delete a directory
# os.remove('pythonCopy.py')

# Generators
# special functions that generate values on the fly as when requested they use yield keyword 
# Generators in Python are a special kind of iterator, defined using functions and the yield statement. 
# They allow you to iterate over a sequence of values lazily, meaning that values are generated on the fly 
# and not stored in memory, which is particularly useful for large datasets or streams of data
# Advantages of Generators
# Memory Efficiency: Generators are memory efficient because they generate items one at a time and do not store the entire sequence in memory.
# Lazy Evaluation: Generators compute values on the fly, which can be useful for handling large data streams or when the complete dataset is not needed at once.
# Pipelining: Generators can be used to pipeline a series of operations, allowing for a clean and readable way to process data in stages.

# Function Caching 
# from functools import lru_cache
# import time 

# @lru_cache(maxsize=None)
# def double(n):
#     time.sleep(5)
#     return n*2

# print(double(10))
# print(double(20))
# print(double(10))
# print(double(20))

# asyncio 

# In Python, both multithreading and multiprocessing are techniques used for achieving concurrency and parallelism, but they differ in how they accomplish this.

# Multithreading:
# Multithreading involves running multiple threads within the same process, sharing the same memory space. Threads are lightweight execution units that share the same memory space, allowing them to communicate easily and efficiently. However, due to Python's Global Interpreter Lock (GIL), multithreading in Python does not fully utilize multiple CPU cores for CPU-bound tasks, as only one thread can execute Python bytecode at a time.

# Multiprocessing:
# Multiprocessing involves running multiple processes simultaneously, each with its own memory space. Processes are independent of each other and do not share memory by default. Instead, they communicate via inter-process communication (IPC) mechanisms like pipes, queues, or shared memory. Multiprocessing in Python bypasses the GIL, allowing multiple processes to run on separate CPU cores concurrently, making it suitable for CPU-bound tasks.

# Example:
# Let's illustrate the difference between multithreading and multiprocessing using a simple example of calculating the square of numbers. We'll compare the execution time for both approaches.

# Multithreading Example:
# python
# Copy code
# import threading

# def square(n):
#     return n * n

# def main():
#     numbers = [1, 2, 3, 4, 5]
#     threads = []

#     for number in numbers:
#         thread = threading.Thread(target=square, args=(number,))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

# if __name__ == "__main__":
#     main()
# Multiprocessing Example:
# python
# Copy code
# import multiprocessing

# def square(n):
#     return n * n

# def main():
#     numbers = [1, 2, 3, 4, 5]
#     pool = multiprocessing.Pool()

#     results = pool.map(square, numbers)
#     pool.close()
#     pool.join()

#     print(results)

# if __name__ == "__main__":
#     main()
# Comparison:
# Multithreading: In this example, each number is squared in a separate thread. However, due to Python's GIL, the execution time may not be significantly faster, especially for CPU-bound tasks.
# Multiprocessing: In this example, each number is squared in a separate process using the multiprocessing.Pool class. This approach fully utilizes multiple CPU cores and may result in faster execution times for CPU-bound tasks.
# Conclusion:
# Use multithreading for I/O-bound tasks (e.g., network operations, file I/O) where threads spend most of their time waiting for I/O operations to complete.
# Use multiprocessing for CPU-bound tasks (e.g., mathematical computations, data processing) that can benefit from parallel execution on multiple CPU cores.
# It's essential to choose the appropriate concurrency model based on the nature of your task and hardware characteristics to achieve optimal performance.

from numpy import copy
import pandas as pd

# Create two sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name': ['Alice', 'Bob', 'Charlie'], 
                    'k' : [1,2,3]})
# print(df1)
# print(df1.loc[0])

# pd.merge(left=, right=, how='left', on='')  # for join 
# merged_df = pd.merge(df_left, df_right, left_on='ID', right_on='CustomerID')
# for common column names we use suffixes by default they are _x and _y
# merged_df = pd.merge(df1, df2, on='ID', suffixes=('_left', '_right'))
# rename column name 

# Rename multiple columns
# df.rename(columns={'A': 'New_Column_Name_A', 'B': 'New_Column_Name_B'}, inplace=True)

# to copy 
# df1 = pd.DataFrame({'A': [1, 2, 3],
#                     'B': [4, 5, 6]})

# # Create a new DataFrame from the original
# df2 = df1.copy()

# series to df -- series.to_frame() 

# df = pd.DataFrame({'Num':[1,1,1,2,3,4,5,6,6,7,8,9,10]})
# print(df[df['Num'].duplicated()].groupby('Num').sum())

# ser1 = pd.Series([10,9,8,7])
# ser2 = pd.Series([5,4,3,2])
# ser3 = ser1 + ser2
# print(ser3)
# print(df.dtypes)

# person.sort_values(by='id', inplace=True)
# person.drop_duplicates(subset=['email'], inplace=True)

# dic = {
#     'name':['A','A','B','B'],
#     'age':[1,2,3,4],
#     'id':[12,11,15,14]
# }
# df = pd.DataFrame(dic)
# print(df.groupby('name').agg(x=('id','min')))

# df = customer[(customer.referee_id != 2) | (customer.referee_id.isnull())]['name']

