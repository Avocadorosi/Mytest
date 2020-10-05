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
       



  
def pos_or_neg(list1):
    neg_count , pos_count = 0,0
    for num in list1: 
          
        # checking condition 
        if num >= 0: 
            pos_count += 1
      
        else: 
            neg_count += 1
    return pos_count, neg_count
        


def Producto(ist) : 
      
    # Multiply elements one by one 
    result = 1
    for x in ist: 
         result = result * x  
    return result  
   
   
   
def separar(string): 
  
    list_string = string.split(' ') 
    return list_string 
  
def juntar(list_string): 
  
    string = '-'.join(list_string) 
    return string 
  
   

if __name__ == "__main__":

    list1 = [1, 212, 23]  
    list2 = [31, 22, 44] 
    print(Producto(list1)) 
    print(Producto(list2)) 
    
    
    #Maybe improve others
    is_prime(1133)
    is_prime(1124)
    is_prime(111)
    
    
    
    list1 = [1048, -217, 64, -455, 646, -933, 12,1] 
    p,s=pos_or_neg(list1)
    print("Positive numbers in the list: ", p) 
    print("Negative numbers in the list: ", s) 
    
    
    
    s = 'Solo una prueba'
      
    # Splitting a string 
    list_string = separar(s) 
    print(list_string) 
  
     # Join list of strings into one 
    s2 = juntar(list_string) 
    print(s2) 