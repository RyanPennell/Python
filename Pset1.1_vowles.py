#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:24:13 2019

@author: ry4n
"""

s = 'azcbobobegghakl'
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"
vowels = 0


for char in s:
        if char in "aeiouAEIOU":
            vowels = vowels+1
            

print("Number of vowels: ", vowels)
