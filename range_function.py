#!/usr/bin/env python
# coding: utf-8

# In[3]:


def my_range(m, n):
    
    empty_list = []
    empty_list.append(m)
    count = m
    
    while count != n:
        count += 1
        empty_list.append(count)
    
    return empty_list[0:-1]

my_range(5, 10)

