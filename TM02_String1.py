# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:20:38 2021

@author: UC17
"""

#Program to count the number of upper and lower case letters in a String

string = "John is driving to Delhi"
count1=0
count2=0

for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
            
print("The number of lowercase letters is:")
print(count1)

print("The number of uppercase letters is:")
print(count2)