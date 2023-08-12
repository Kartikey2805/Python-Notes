# Everything in Python is an object
# print(1 + 2)
# print((1).__add__(2))
# Above 2 statements are same

# Start a particular version of python by following commands

# py --list (all versions installed)
# py --list-paths
# py --version
# py -3.9 (start a session using particular python version)
# py - will use default verison of python

# Floats do not have exact representation
# like 0.1 is represented as 0.9999999....
# format(0.1,'.25f')
# 0.1 + 0.1 == 0.2 // output is False

# datatypes are objects
# they have state and functionality
# int is an object, uses __add__ to add a number

# Dictonaries - hashMaps (Mutable)

import csv
from datetime import datetime
dict = {
    'a': 97,
    'b': 98
}

# print(dict['a'])

# ----- iterate in dictinary ----

# for key in dict:
#     print(key)

# for values in dict.values():
#     print(values)

# for key,values in dict.items():
#     print(key)
#     print(values)

# -----check a value in dictionary----
# if 'c' in dict:
#     print('TRUE')

# dict.clear()
# newDict = dict.copy() ## shallow copy --- reference
# newDict = dict(a = 1, b = 2)
# print(newDict)

# d = dict.fromkeys(['a','b'],0)
# print(d)

# dict.get('a','defaultValue')  ## return key value if key exits otherwise default

# merge one dictionary into other
# d1 = {'a':1,'b':2}
# d2 = {'b':3,'c':4}
# d1.update(d2) ## d1 = {a:1,b:3,c:4}
# print(d1)

#  --------- SETS  ------ (only unique values)

s = {1, 'a', True}
# s = set([1,'a',True])
# s = set()  ## empty set, if s = {} it would be a dictionary
# print(s)

# l = [1,1,1,2,2,2,2,3,3]
# s = set(l) ## only contains unique elements
# print(s)

# s = set('GOEL') ## s = {G,O,E,L}
# print(s)

# set operations

# 1. isdisjoint -- s1.isdisjoint(s2)
# 2. add --- s1.add(4)
# 3. remove --- s1.remove('a')
# 4. discard -- s1.discard('a')

# s1 < s2 -- strict subset
# s1 <= s2 -- subset
# s1 > s2 -- strict superset
# s1 >= superset

# Union
# s1 | s2 ## union of s1 and s2
# s1 & s2 ## intrersection
# s1 - s2 ## in s1 but not in s2

###############  comprehensions (alternate of iterables) ##########
nums = [1, 2, 3, 4, 5]
# list comprehensions
# squareOfNums = [number ** 2 for number in nums if number % 2 == 0]
# print(squareOfNums)

# sets and dictionary comprehensions
# set
# s  = {number ** 2 for number in nums if number % 2 == 0}

# d = {keys[i]:values[i] for i in range(len[keys]) if values[i] > 0}

############ Exceptions #############
# There is a hierarchy in exceptions
# we can handle a specific exception more precisely
# eg - IndexError, SyntaxError, KeyError, ZeroDivisionError, ValueError, TypeError, FileNotFoundError

a = 1
b = 0
# try:
#     res = a/b
#     print(res)
# except ZeroDivisionError as exp:
#     print(exp)
# except IndexError as exp:
#     print(exp)
# finally:
#     print('this executes always no matter what')

# print(res)
# repr(exception)  ## object key value
# print(exception) ## only value

# --------------     Iterators   --------------------#

# l = [num for num in range(1, 10)]
# iterator = iter(l)

# try:
#     while True:
#         print(next(iterator))
# except StopIteration:
#     pass

# EG - list() returns iterable (it is an object while enumerate returns a iterable)

# -------- Generators ------------
# They are iterators (implement next() function)
# eg - (i**2 for in range(10))  --- create a generator
# They use lazy iteration - calculated only when requested
# they are memory efficient

# l = range(10)
# print(3 in l, 1 in l)
# itr = iter(l)
# print(next(itr))
# r = list(itr)
# print(r)


# ****************** Functions *******************

# print(datetime.now().weekday())

# *args in functions is a tuple - arguments
# default values comes to right (except for *args)
# def func(a=1,*args):  # this will work
#     print(a)
#     print(args)

# def func(a=1,b,*args):  # this will not work
# print(a)
# print(args)

# func()

# **kwargs - keyword arguments - it is a tuple

# Lambda functions --  returns function -- shorter expression

# f = lambda a,b:a+b
# print(f(1,2))

# ------------ filter -----------------

# l = list(range(10))
# evens = filter(lambda a: a % 2 == 0,l)
# print(list(evens))

# ----------- sorting -------------

# data = [-1,2,8,10,9,4,65,56]
# print(sorted(data,reverse=True))


# ------------- Decorators ---------------


# ------------   Files (CSV Module) ------------


# with open('file1.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"', escapechar="\\")
#     for row in reader:
#         print(row)

# dialect -- uses for providing pre defined settings in csv reader for not typing settings again and again

# csv.list_dialects()

# csv.register_dialect('pdv', delimiter=",", quotechar='"', escapechar="\\")

# print(csv.list_dialects())

# with open('file1.csv', 'r') as f:
#     reader = csv.reader(f, dialect="pdv")
#     for row in reader:
#         print(row)

# data = [['a', 'a', 'a'], ['b', 'b', 'b']]

# with open('file1.csv', 'a') as f:
#     writer = csv.writer(f, dialect="pdv", quoting=csv.QUOTE_ALL)
#     for row in data:
#         writer.writerow(row)


# ------------ Classes ------------

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def outputRadius(self):
#         print(self.radius)

# special methods like __eq__
#     def __eq__(self, other):
#         return self.radius == other.radius

# c1 = Circle(2)
# c2 = Circle(2)

# print(c1 == c2) #return True ( because of re defining __eq__ method in Circle class otherwise False)
# c1 == c2 is equivalent to c1.__eq__(c2)
