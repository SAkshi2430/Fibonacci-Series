# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("FIBONACCI SERIES")
print("Enter a no. upto where fibonacci series to be printed.")
n=int(input())
i=0
j=1
x=1
print(i)
while(x<=n-1):
    sum=i+j
    print(sum)
    j=i
    i=sum
    x+=1
    
    
    
