#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:16:51 2018
1) class{variable+functions} <--> objects{variable+functions}
define a Class -- create objects -- access objects through variables and functions
2) name scope
@author: yongweiw
"""

#import script1
#
#print("script2's name:{}".format(__name__))

#assert 2 + 2 == 5, "2+2=5 not true!"

""" ***************** class--objects ****************"""
# define a class to describe students' skills
"__init__(self, [,args...]) constructor with any optional arguments, called as \
obj = className(args)"

class StuInfo:
    # __init__()
    def __init__(self, name):
        self.name = name
        self.skills = []  # all variables used in Class must be initialized
    
    def add_skills(self, skill):
        self.skills.append(skill)

# 0) create objects        
Stu_1 = StuInfo("Anna")
Stu_2 = StuInfo("Jack")

# 1) access functions with operations
Stu_1.add_skills("playing the panio")
Stu_1.add_skills("playing the guitar")
Stu_1.add_skills("playing chess")

Stu_2.add_skills("playing ping-pang")
Stu_2.add_skills("playing dota")


# 2) access variables
print("Stu_1's info. Name:{}, skills:{}".format(Stu_1.name,Stu_1.skills))
print("Stu_2's info. Name:{}, skills:{}".format(Stu_2.name,Stu_2.skills))

# another class example, include more detailed information
class StuInfo_full:
    'common base class for all students'
    stuCount = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        StuInfo_full.stuCount += 1
        self.skills = []
    
    def displayCount(self):
        print("Total students %d" % StuInfo_full.stuCount)
        
    def displayStu(self):
        print("Name:", self.name, ", Age: ", self.age)
    
    def add_skill(self, skill):
        self.skills.append(skill)
        
"Create the first object based on StuInfo_full class"
Stu_1_full = StuInfo_full("Anna", 8)
Stu_1_full.add_skill(["piano","guitar","chess"])
"Create the second object based on StuInfo_full class"
Stu_2_full = StuInfo_full("Jack", 9)
Stu_2_full.add_skill(["ping-pang","dota"])        
"add items to students"
Stu_1_full.stuNo = 123
Stu_2_full.stuNo = 456

"operate on two objects"
Stu_1_full.displayStu()
Stu_2_full.displayStu()
print("Total students %d" % StuInfo_full.stuCount)
print("Stu1 number: %d" % Stu_1_full.stuNo)

"built-in attributes"
print("StudInfo_full.__doc__",StuInfo_full.__doc__)
print("StudInfo_full.__name__",StuInfo_full.__name__)
print("StudInfo_full.__module__",StuInfo_full.__module__)
print("StudInfo_full.__bases__",StuInfo_full.__bases__)
print("StudInfo_full.__dict__",StuInfo_full.__dict__)

"*******class inheritance*********"
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

# iterators
for element in [1,2,3]:
    print(element)
    
for element in (4,5,6):
    print(element)

for key in {'one':1,'two':2}:
    print(key)
    
for char in "123":
    print(char)
    
for line in open("myfile.txt"):
    print(line, end='')

# built-in Python iterator implemented using Class   
class Reverse():
    """ Iterator for looping over a sequence reversely"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
    
# create an object with Reverse 
revSeq = Reverse("ABCD")
print("")
#print(revSeq.data)
print(iter(revSeq))
for char in revSeq:
    print(char)
        
      