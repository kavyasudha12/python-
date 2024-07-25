# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:25:07 2024

@author: gelli
"""

arr=[1,1,0,1,1,0,0]
ones=[]
zeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        ones.append(i)
zeros.extend(ones) 
print(zeros)