#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math #for some functions we need
def solve_quadratic(a, b, c):
    
    #we calculate discriminant first
    discriminant = b*b - 4*a*c
    #taking square root of discriminant
    sqrt_dis = math.sqrt(abs(discriminant))
    
    if discriminant > 0:
        print((-b + sqrt_dis)/(2*a))
        print((-b - sqrt_dis)/(2*a))
    
    elif dis == 0:
        print(-b/(2*a))
        
    else:
        print("There is no real root (complex roots).")
    
    ## edge case to solve when a = 0
    
#if a == 0:
    #print("Incorrect input, use the correct equation!")
#else: 
    #solve_quadratic(a, b, c)

solve_quadratic(1, 10, -24)

