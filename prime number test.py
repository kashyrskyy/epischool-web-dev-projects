#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_prime(n):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                return False # not a prime number
        else:
            return True # a prime number
    else:
        return False # not a prime number

