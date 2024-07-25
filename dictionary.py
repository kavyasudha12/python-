# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:51:21 2024

@author: gelli
"""


s='hello good morning hello good morning'

s=s.split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s1=''
for k,v in d.items():
    if v>=1:
      s1+=k+' '
print(s1)
        