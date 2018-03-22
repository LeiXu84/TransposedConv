#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:16:51 2018

@author: yongweiw
"""

#import script1
#
#print("script2's name:{}".format(__name__))

#assert 2 + 2 == 5, "2+2=5 not true!"

"""1)***************** class--objects ****************"""
# define a class to describe students' skills
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
print(Stu_2.skills)
print("Stu_2's info. Name:{}, skills:{}".format(Stu_2.name,Stu_2.skills))


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
        
       