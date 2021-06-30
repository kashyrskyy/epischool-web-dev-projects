#!/usr/bin/env python
# coding: utf-8

# In[2]:


def reverse_list(list_input):
    reversed_list = []
    
    for i in list_input:
        reversed_list.append(list_input[-i])
        
    return reversed_list

reverse_list([1,2,3,4])

