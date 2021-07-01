#!/usr/bin/env python
# coding: utf-8

# In[8]:


## (1)

def primes_below(n):
    
    output_list = []
    
    for i, x in range(2, n):
        if i % x != 0:
            output_list.append(i)
    
    return output_list


# In[10]:


## (2)

def is_prime(n):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                return False # not a prime number
        else:
            return True # a prime number
    else:
        return False # not a prime number

def print_prime(n):
    
    primes_list = []
    
    for i in range(2, n+1):
        if is_prime(i): # if True
            primes_list.append(i)
            
    return primes_list

## test
print_prime(100)


# In[ ]:




