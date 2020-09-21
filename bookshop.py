# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:11:02 2020

@author: HP
"""

from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],[2, ("5464", 9, 9.99), ("9744", 9, 44.95)],[3, ("5464", 9, 9.99), ("88112", 11, 24.99)],[4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

invoice = list(map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders)))

#Breaking

'''
output1=map(lambda y:y[1]*y[2] ,x[1:])
output2=list(map(lambda y:y[1]*y[2] ,x[1:]))
output3=reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))
output4=map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:]))))
output5=map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders))
output6=list(map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders)))
'''
