# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:31:29 2020

@author: HAR$H yadav
"""
for i in range(100,300):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime==True:
        print(i)