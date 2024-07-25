# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 09:57:11 2024

@author: gelli
"""

s='abcdz'
#output should be bcdea

s1=''
for c in s:
    if ord(c)>=97 and ord(c)<122:
        s1+=chr(ord(c)+1)
    else:
        s1+=chr(ord(c)-25)
    print(s1)

    