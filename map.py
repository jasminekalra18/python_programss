# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:05:42 2020

@author: HP
"""

list1=[1,2,3,4]
res=[]
for i in list1:
    res.append(i+20)
print(res)
#map fun is used to map input to o\p based on function
#syntax: map(function,agruements)
list1=[1,2,3,4,5]
 #function
def add_num(x):
    return x+20
map(add_num,list1)
print(type(map(add_num,list1)))
#typecasting into list or tuple format
rex=tuple(map(add_num,list1))
print(rex)

list1=[1,2,3,4]
y=map(lambda x:x+20,list1)
print(list(y))
