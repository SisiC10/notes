# SYNTAX

#this is commenting single lines

"""this
is commenting 
multiple lines"""

# *PRINTING VARIABLES
#a = 10
#print (a)

# *SLASHES TO CREATE PLACEHOLDERS (CONTINUE ON NEXT LINE)
# total = 1 + \
#    2 + \
#        3
# print(total)

# *MILTIPLE PRINTS
# var = 'hacker'
# print (var)
# var = "programmer"
# print(var)

# *MULTIPLE LINES
# var = """thank 
# you
# for 
# watching"""
# print (var)

# a = input()
# print(a)

# *USER INPUT 
# a = input("Enter your name")
# print (a)

# *MULTIPLE STATEMENTS IN A SINGLE LINE
# a = 1; b = 1; c = 3; print(a,b,c)

# *SWAP TWO INTEGERS
# a = 1; b = 2;
# a,b = b,a
# print(a,b)

# VARIABLES AND DATA TYPES

#VARIABLE DECLARATION - in python a variable is created as soon as its assigned a value (=), it does not need a command.

# x = 10
# y = 20
# print(x+y)
# print(x*y)

# DATA TYPES (6):

#  1. NUMBERS:
# x = 10j
# print(type(x)) 
# *will show its an integer if no decimal, float if decimal & complex ifvariable added

# num = 10>9
# print(type(num))
# print(num)
# * shows 'bool' and true

# 2. STRING:
# name = "jack"
# print(len(name))
# # *shows 4

# print(name[2])
# # *shows c - third letter in jack since j is 0

# print(name[0:5])
# # *prints 'jack'
# print(name.upper())
# # *prints 'JACK'

# 3. LISTS:
# mylist = [10, 20, 30, 'hacker', 'programmer']
# print(mylist[2:5])
# # prints last 3 items

# mylist[3]=40
# print(mylist)
# # adds 40 to third spot in the list

# mylist.append(10)
# print(mylist)
# # adds 10 to the end of list

# mylist.insert(5,100)
# print(mylist)
# # adds 100 to fifth spot

# mylist.reverse()
# print(mylist)
# # reverses list!

# 4. DICTIONARY:
# courses = {1: 'python',
# 2: 'data science',
# 'three': 'machine learning'}
# print(courses)

# print(courses['three'])
# print(courses.get('three'))

# courses['four']='BCA'
# print(courses)

# 5. TUPLES:
# animal = (10,10,20,'tiger','lion','giraffe','tiger')
# print(animal[2])
# print(animal.count('tiger'))

# 6. SETS:
# myset = (10,20,30,40,50,'hacker','programer')
# print(myset[2])
# # prints '30'

# print(range(10))
# # prints 'range(0,10)'

# print(list(range(10)))
# # prints '[0,1,2,3...10]

# a = [1,2,3,4]
# b = {5,6,7,8}
# c = [a,b]
# print(c)
# # prints '[[1, 2, 3, 4], {8, 5, 6, 7}]'

# TYPE CONVERSION using data types 1-6
# x = 10
# name = 'name'
# # print(x+name) * will not work

# print(str(x)+name)
# # * will work


# IF AND ELIF STATEMENTS:

# PYTHON CONDITIONS ie. condition, if true (elif)/if false (else).
# x = int(input('Enter a number: '))

# if x % 2 == 0:
#     print('even number')
# elif x % 2 != 0:
#     print('odd number')
# else:
#     print('try again')
# if the number divided by 2 is equal to 0 (even) & if it is not equal to(!) 0 (odd).

# if x > 0:
#         for i in range(2,x):
#             if x % 2 == 0:
#                 print('not a prime number')
#                 break
#             else:
#                  print('prime number')
#                  break
# else:
#      print('give a positive number')

# SHORTHAND IF/ELSE:
# x = int(input('Enter a number '))
# y = int(input('Enter a number '))

# print('Greater') if x>y else print('Smaller')

# COMPLEX IF/ELSE:
# if x > y:
#     if:
#         if:
#             if:

# x =int(input('Enter a number '))

# if x > 0 and x<10 :
#     if x < 5:
#         print('Less than 5')
#     else:
#         print('Greater than 5')
# elif x >= 10:
#     print('Greater than or equal to 10')
# else:
#     print('enter a number again')
  

  # WHILE LOOPS:

# print('hacker')
# # will print once

# i = 1
# while i <= 5:
#     print('hacker', i)
#     i = i+1
# # prints 5X

# i = 1
# while i <= 5:
#   print('hacker',end=' ')
#   j = 1
#   i = i+1
#   while j <= 4:
#       print('programmer', end=' ')
#       j = j+1
#   print()


# FOR LOOPS:

# x = ['sierra',65,2.5]
# print(x)
# # will print values one-by-one

# x = ['sierra',65,2.5]
# for i in x:
#     print(i)
# # will print on own lines

# x = 'sierra'
# for i in x:
#     print(i)
# # will print letters on seperate lines

# for i in [2,6,'ball']:
#     print(i)

# for i in range(10,21):
#     print(i)

# for i in range(10,21,2):
#     print(i)
# # increments of 2

# for i in range(20,9,-1):
#     print(i)
# # backwards

# for i in range(1,20):
#     if i%5 != 0:
#         print(i)


# PATTERNS:

# # We can do:
# print('* ',end="")
# print('* ',end="")
# #.. over and over to get a 4X2 * block OR:

# for j in range(4):
#   print('* ',end="")

# print()
# for j in range(4):
#   print('* ',end="")

# # OR:
# for x in range(2):
#   for y in range(4):
#     print('* ',end="")

#   print()

# # to get a half pyramid:

# for i in range(10):
#   for j in range(i+1):
#     print('* ',end="")

#   print()

# # to get upside down half pyramid:

# for i in range(4):
#   for j in range(4-i):
#     print('* ',end="")

#   print()

# # random string function XD:
# var1 = 'Hello World!'
# print(var1[:6] + 'Python')

# CLASSES:
#  allows grouping of data and functions in a way thats easy to reuse and build upon.

#   INSTANCE VARIABLES (NO INIT):

# class Employee:
#     pass
# # use pass to leave class empty

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey.schafer@company.com'
# emp_1.pay = 50000
 
# emp_2.first = 'Sally'
# emp_2.last = 'Chase'
# emp_2.email = 'Sally.Chase1@company.com'
# emp_2.pay = 53000

# print(emp_1.email)
# print(emp_2.email)


# INSTANCE VARIABLES WITH INIT: allows for easier use
# class Employee:
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Sally', 'Chase', 55000)

# print(emp_1.first)
# print(emp_2.email)

# # print(emp_1.first, emp_1.last)
# # print('{} {}'.format(emp_1.first, emp_1.last))
# # both are the same as line before it but unecessary when defined under the class (line 330,331). So:
# print(emp_1.fullname())
# # OR:
# print(Employee.fullname(emp_1))


# CLASS VARIABLES: something that would be the same to every variable within the class, ie. a yearly 4% increase in pay for employees:

# class Employee:
    
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Sally', 'Chase', 55000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# # can print either way to see how much the pay was raised (4%).

# # you can CHANGE the raise amount or a single employees raise amount via: emp_1.raise_amount = ____

# print(emp_1.__dict__)
# # will print all attributes including any changes made.


# CLASS VARIABLE WITHOUT USING SELF:
 
# class Employee:
    
#     num_of_emps = 0
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)

# print(Employee.num_of_emps)

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Sally', 'Chase', 55000)

# print(Employee.num_of_emps)


# CLASS METHODS: in regular class method, it automatically takes in the instance however it can be made so that the class is taken as the first argument instead:
# import datetime

# class Employee:
    
#     num_of_emps = 0
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
    
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount
# # adding this alters the functionality of the method to where now we recieve the class (cls) as the first argument instead of the instance(self): 

#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#     # You can also use class methods as alternative constructors; provides multiple ways of creating objects,
#     # ex.  employee information is in strings seperated by hyphens and need to pass them before creating new employees, instead want to create a new employee from it:

#     @staticmethod
#     def is_workday(day):
#       if day.weekday() == 5 or day.weekday() == 6:
#         return False
#       return True
# # STATIC METHODS: functions put into classes. EX; a function that takes a date and determines whether its a workday (doesnt depend on any instance or class variable):
#         # typically it is static when the instance or class is not accessed within the function.

# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Sally', 'Chase', 55000)

# my_date = datetime.date(2016, 7, 10)

# print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05)
# # this is now a class method instead of the instance so it changes all employees raise amounts(prints 1.05 instead of 1.04). Thus we dont have to right out 'Employee.cls_amt = ___:
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(Employee.raise_amt)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-50000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# # class methods rundowns: regular methoda automatically pass the instance as the first argument(self), class methods automatically pass the class as the first argument (cls), static methods dont pass either automatically and behave like regular functions but are put into classes.

# # INHERITANCE: creating types ie, employees that are developers or managers.

# class Employee:
    
#     num_of_emps = 0
#     raise_amount = 1.04
    
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + "." + last + '@company.com'

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)

# class Developer(Employee):
#     raise_amount = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
    
#     def apply_raise(self):
#         self.pay = int(self.pay * Developer.raise_amount)

# class Manager(Employee):
    
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#     # accepts first, last, pay & list of employees that the manager supervises
    
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     # can remove employees from list of employees

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#     # prints out all employees

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())

# emp_1 = Employee('Corey', 'Schafer', 50000)
# dev_1 = Developer('Sally', 'Chase', 55000, 'Java')
# mgr_1 = Manager('Sue', 'Smith', 90000, [emp_1])

# print(emp_1.email)
# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.raise_amount)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.raise_amount)

# print(mgr_1.email)
# mgr_1.add_emp(dev_1)
# mgr_1.print_emps()

# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager,Employee))
# print(issubclass(Employee, Developer))