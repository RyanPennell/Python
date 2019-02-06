#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:07:18 2019

@author: ry4n
"""

s="abcpqoiweurpoiqwuerpoiqefghi.,zmxnc,v.mznxcvpoiwuertoiuwerotiuweropitulkajshdfkjashdkfjhasdkjfhasd"

def longest_ascending(s):
    matches = []
    current = [s[0]]
    for index, character in enumerate(s[1:]):
        if character >= s[index]:
            current.append(character)
        else:
            matches.append(current)
            current = [character]
    matches.append(current)
    return "".join(max(matches, key=len))
print(longest_ascending(s))
