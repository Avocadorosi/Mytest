#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:27 2020

@author: ros

"""
def is_prime(num):
    if num > 1:        
       for i in range(2, num): 
           if (num % i) == 0: 
               return False
               break
       else: 
           return True
    else: 
       return False
       




def Suma(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum


#Maybe improve others
is_prime(113)