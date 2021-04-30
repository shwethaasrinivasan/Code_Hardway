# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

list1 = []
for i in range(5,-1,-1):
#for i in reversed(range(6)):
    list1.append(i)
    print(list1)
j = ''.join(str(i) for i in list1)
print(j)
list1.append([9,8,14])
list1.remove([9,8,14])
print (list1[5])
list1.insert(6,9)
print("list without sorting ",list1)
# print (sorted(list1))
i=0
while i<len(list1):
    key=i
    print("key",key)
    j=i+1
    print("j",j)
    while j<len(list1):
        if list1[key]>list1[j]:
            key=j
            print("inner key",key)
        j+=1
        print("inner j",j)
        print ("inner list",list1)
    list1[i],list1[key]=list1[key],list1[i]
    print ("i","key",list1[i],list1[key])
    print ("key","i",list1[key],list1[i])
    i+=1
    print ("inner list2",list1)
    print("i",i)
print("list after sorting ",list1)