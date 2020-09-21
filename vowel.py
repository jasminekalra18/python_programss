# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:04:16 2020

@author: HP
"""

def rem_vowel(list):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in list.lower():
        if x in vowels:
            list = list.replace(x, "")


    print(list)


# Driver program
list= [ 'Alabama', 'California', 'Oklahoma', 'Florida']
rem_vowel(list) 