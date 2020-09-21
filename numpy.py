# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:14:07 2020

@author: HP
"""

import numpy as np
a=np.array([1,2,3])
print(a)
print(a[::-1])#reverseslicing
print(a[-1])
print(a.shape)
print(a.size)
b=np.array([[1,2,3,4],[6,7,8,9]])
print(b)
print(b[1,2])
print(b.shape)
print(b.size)
import pandas as pd
#1d series 2d framework
a=np.array(['g','o','l','u'])
print(a)
print(type(a))
x=pd.Series(a)
print(x)
p=x.values
print(p)
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[20,30,40,50,60]
plt.plot(x,y)
