# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:33:37 2021

@author: UC17
"""
#Program that takes a string and prints the letters in decreasing order of frequency

W= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(W))