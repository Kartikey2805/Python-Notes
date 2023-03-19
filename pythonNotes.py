fruit = 'Orange';
# print(fruit[7])

# def getName():
#     return 'John'

# print(len(getName()))

# Everything in python is an object
# For eg: 'string' is an object of type str with methods along with it
# code should be indented in python

# string
print(fruit.upper())

# string multiplication
print('-'*10)

# string concatenation
happiness = 'happy '*3
quote = 'I love my Country'
print(happiness)

# convert number to string 
version = 3
print('I love python ' + str(version))

var1 = 'I'
var2 = 'love'
var3 = 'Python'

print('{0} {1} {2}. {2} {1} {0}'.format(var1,var2,var3))

print('{0:10} | {1:10}'.format('Name','Age'));
# < represents left alignment, > represents right alignment
# {0:10} represents take 1st argument and make it 10 characters long
print('{0:10} | {1:<10}'.format('John',33))  

# .2f represents gives us 2 decimal places after the number
print('{0:<8.2f}'.format(2.33333))

# take input
# fruit = input('Enter your favourite fruit: ')
# print(fruit)

print(4/2)

# convert string to number
print(1+int('3'));
print(1+float('3'));


# Functions

def oddOrEven(number):
    """returns whether a number is odd or even""" 
    if(number % 2 == 0): return 'Even'
    else: return 'Odd'

print(oddOrEven(5))

# listVars

listVar = [1,2,3,4,5]

# listVar slicing
print(listVar[1:1])
# listVar.extend([6,7])  # add 6, 7 to the listVar
listVar.insert(6,6)

print(listVar)

# exception handling

try:
    index = listVar.index(7)
except:
    index = 'Value does not exist'

print(index)

# loops

for number in listVar:
    print(number)

index = 0
while index < len(listVar):
    print(listVar[index])
    index += 1

# for number in range(3)  // 1,2
# for number in range(1,3) // 1,2 
# for number in range(1,10,2) // 1 3 5 7 9

# dictionaries
# data structure that contains key value pairs

dictionary = {"key1":'value1',"key2":'value2'}

print(dictionary["key1"])

# update a record
# dictionary['key1']='value11'

print(dictionary["key1"])

# insert a record
dictionary['key3']='value3'
print(dictionary["key3"])

# delete a record
del dictionary['key3']

print(dictionary)

for keys in dictionary:
    print(dictionary[keys])

# find a record in dictionary
if 'key1' in dictionary.keys():
    print('yes')

if 'value1' in dictionary.values():
    print('yes')

#  tuples
# they are immutable i.e once defined cannot be changed
# they are ordered
# values can be accessed by index 
# looping, concatenation possible
# use when data should not change

tuple1 = (1,2,3,4,5)
tuple2 = (1,)

days_in_a_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

# delete whole tuple 
# del days_in_a_week

# convert tuple to list

tupleList = list(days_in_a_week)
print(tupleList)

for item in days_in_a_week:
    print(item)

# Files 

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist (append, does not overwrite)

# "w" - Write - will create a file if the specified file does not exist

# "r" - read file 

# 'b' - binary mode 

# 't' - text mode

# for eg - open('path to file','rb')
 
#creating a text file with the command function "x"

f = open("data.txt", "r")
print(f.tell())
print(f.read())
print(f.tell())

# seek - set pointer back to begining of file 
f.seek(0)
print(f.read())
f.close()

# delete a file 
# import os
# os.remove('myFile.txt')

# Check if file exists, then delete it:
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# Remove the folder "myfolder":
# import os
# os.rmdir("myfolder")

# automatically closes a file stream
# a+ means append + read mode
# r+ means write and read (here file will be overwrited not appended)
# a - will only append and create file if it does not exits 

with open('data.txt','a+') as file:
    file.write('\nI am also good')
    for line in file:
        print(line.rstrip())
    print(file.read())
    print(file.closed)

print(file.closed)