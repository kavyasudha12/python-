# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:38:46 2024

@author: gelli
"""

#Removing the duplicate words
s='hello good morning hello good morning'
s=s.split()
s1=' '
for i in s:
    if i not in s1:
        s1=s1+i+' '
print(s1)