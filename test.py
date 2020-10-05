#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:27 2020

@author: ros

"""

def Suma(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum


def is_prime(num):
    es = False
    if num > 1:        
       for i in range(2, num): 
           if (num % i) == 0: 
               es = False
               break
       else: 
           es=True
    else: 
       es = False
    return es
       



def Producto(ist) : 
      
    # Multiply elements one by one 
    result = 1
    for x in ist: 
         result = result * x  
    return result  
   
   
# Driver code 
list1 = [1, 22, 3]  
list2 = [31, 2, 44] 
print(Producto(list1)) 
print(Producto(list2)) 


#Maybe improve others
is_prime(113)
is_prime(112)
is_prime(111)