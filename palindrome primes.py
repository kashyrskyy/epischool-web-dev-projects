#!/usr/bin/env python
# coding: utf-8

# In[11]:


def big_fibonacci(n):
    
    fibonacci_list = []
    
    if n < 0:
        return False
    
    n1 = 0
    fibonacci_list.append(n1)
    n2 = 1
    fibonacci_list.append(n2)

    while len(str(fibonacci_list[-1])) < n + 1 and len(str(fibonacci_list[-1])) > n - 1:
        nth = n1 + n2
        n1 = n2
        big_fibonacci.append(nth)
    
    return fibonacci_list[0]


# In[12]:


big_fibonacci(10)

