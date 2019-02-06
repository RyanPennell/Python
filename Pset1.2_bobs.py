#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:02:27 2019

@author: ry4n
"""

s = 'azcbobobegghakl'
bob=0
for i, _ in enumerate(s): 
    if s[i:i+3] == 'bob': 
        bob += 1
print('Number of times bob occurs is: ' + str(bob))