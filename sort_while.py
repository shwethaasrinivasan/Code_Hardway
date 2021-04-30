# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:18:56 2021

@author: Barathwaj Kesavan
"""

a=[12,0,39,50,1]
i=0
while i<len(a):
    key=i
    j=i+1
    while j<len(a):
        if a[key]>a[j]:
            key=j
        j+=1
    a[i],a[key]=a[key],a[i]
    i+=1
print(a)


