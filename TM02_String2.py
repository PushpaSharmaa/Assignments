# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:07:38 2021

@author: UC17
"""

#Program that will check whether a given String is a Palindrome or not

string1 = "malayalam"

if (string1 == string1[::-1]):
    print("The given String is a Palindrome")
    
else:
    print("The given String is not a Palindrome")
    