# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:05:25 2020

@author: HP
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
